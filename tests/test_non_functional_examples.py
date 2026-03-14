from datetime import UTC, datetime, timedelta
import time
import unittest

from _helpers import ROOT  # noqa: F401
from virtual_campus.app import build_demo_environment
from virtual_campus.entities import User
from virtual_campus.security import hash_password


# Crea usuarios de prueba para simular una carga ligera sobre el servicio.
def _seed_users(user_repository, total_users: int) -> list[str]:
    emails: list[str] = []
    for index in range(total_users):
        email = f"estudiante{index}@lasalle.edu.co"
        user_repository.save(
            User(
                email=email,
                password_hash=hash_password(f"ClaveInicialSegura{index}!"),
            )
        )
        emails.append(email)
    return emails


class PasswordResetLoadExampleTests(unittest.TestCase):
    # Verifica que una ráfaga de flujos completos siga siendo ágil en memoria.
    def test_light_burst_of_complete_flows_stays_under_smoke_threshold(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        user_repository = environment["user_repository"]
        notifier = environment["notifier"]
        audit_log = environment["audit_log"]

        total_users = 200
        emails = _seed_users(user_repository, total_users)

        start = time.perf_counter()

        for email in emails:
            request_result = service.request_password_reset(email)
            self.assertTrue(request_result.success)

        issued_tokens = {
            message.recipient: message.metadata["token"]
            for message in notifier.sent_messages
        }

        for index, email in enumerate(emails):
            reset_result = service.reset_password(
                email=email,
                token=issued_tokens[email],
                new_password=f"NuevaClaveSegura{index}!",
            )
            self.assertTrue(reset_result.success)

        elapsed = time.perf_counter() - start

        self.assertEqual(len(notifier.sent_messages), total_users)
        self.assertEqual(len(audit_log.events), total_users * 2)
        self.assertLess(
            elapsed,
            2.5,
            "El ejemplo de carga ligera supero el umbral didactico de 2.5 segundos.",
        )


class PasswordResetUsabilityExampleTests(unittest.TestCase):
    # Confirma que el mensaje inicial no confunda ni revele si el correo existe.
    def test_request_message_is_consistent_for_known_and_unknown_accounts(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]

        known_result = service.request_password_reset("estudiante@lasalle.edu.co")
        unknown_result = service.request_password_reset("no-existe@lasalle.edu.co")

        self.assertTrue(known_result.success)
        self.assertTrue(unknown_result.success)
        self.assertEqual(known_result.message, unknown_result.message)
        self.assertIn("recuperar tu contrasena", known_result.message.lower())

    # Revisa que la notificación indique con claridad cuál es el siguiente paso.
    def test_notification_message_explains_the_next_step(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        notifier = environment["notifier"]

        service.request_password_reset("estudiante@lasalle.edu.co")
        notification = notifier.sent_messages[0]

        self.assertEqual(notification.subject, "Recuperacion de contrasena")
        self.assertIn("Usa el token recibido", notification.body)
        self.assertEqual(notification.recipient, "estudiante@lasalle.edu.co")

    # Valida que el sistema entregue una guía útil cuando la contraseña no cumple.
    def test_password_policy_feedback_is_actionable(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        notifier = environment["notifier"]

        service.request_password_reset("estudiante@lasalle.edu.co")
        token = notifier.sent_messages[0].metadata["token"]

        reset_result = service.reset_password(
            email="estudiante@lasalle.edu.co",
            token=token,
            new_password="SinNumero!",
        )

        self.assertFalse(reset_result.success)
        self.assertEqual(
            reset_result.message,
            "La contrasena debe incluir al menos un numero.",
        )


class PasswordResetSecurityExampleTests(unittest.TestCase):
    # Comprueba que un token vencido no pueda usarse para cambiar la contraseña.
    def test_expired_tokens_are_rejected(self) -> None:
        current_time = [datetime(2026, 1, 1, 8, 0, tzinfo=UTC)]
        environment = build_demo_environment(now_fn=lambda: current_time[0])
        service = environment["service"]
        notifier = environment["notifier"]

        service.request_password_reset("estudiante@lasalle.edu.co")
        token = notifier.sent_messages[0].metadata["token"]
        current_time[0] = current_time[0] + timedelta(minutes=16)

        reset_result = service.reset_password(
            email="estudiante@lasalle.edu.co",
            token=token,
            new_password="NuevaClaveSegura123!",
        )

        self.assertFalse(reset_result.success)
        self.assertIn("token", reset_result.message.lower())

    # Asegura que cada token sea de un solo uso y no pueda reutilizarse.
    def test_used_tokens_cannot_be_reused(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        notifier = environment["notifier"]

        service.request_password_reset("estudiante@lasalle.edu.co")
        token = notifier.sent_messages[0].metadata["token"]

        first_reset = service.reset_password(
            email="estudiante@lasalle.edu.co",
            token=token,
            new_password="NuevaClaveSegura123!",
        )
        second_reset = service.reset_password(
            email="estudiante@lasalle.edu.co",
            token=token,
            new_password="OtraClaveSegura123!",
        )

        self.assertTrue(first_reset.success)
        self.assertFalse(second_reset.success)
        self.assertIn("token", second_reset.message.lower())

    # Verifica que la auditoría no conserve el valor sensible del token emitido.
    def test_audit_log_does_not_store_raw_reset_tokens(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        notifier = environment["notifier"]
        audit_log = environment["audit_log"]

        service.request_password_reset("estudiante@lasalle.edu.co")
        token = notifier.sent_messages[0].metadata["token"]
        service.reset_password(
            email="estudiante@lasalle.edu.co",
            token=token,
            new_password="NuevaClaveSegura123!",
        )

        for event in audit_log.events:
            self.assertNotIn("token", event.details)
            self.assertNotIn(token, str(event.details))


if __name__ == "__main__":
    unittest.main()
