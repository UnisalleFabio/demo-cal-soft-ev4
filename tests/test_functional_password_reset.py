import unittest

from _helpers import ROOT  # noqa: F401
from virtual_campus.app import build_demo_environment
from virtual_campus.security import hash_password


class PasswordResetFunctionalTests(unittest.TestCase):
    def test_user_can_request_and_reset_password(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        notifier = environment["notifier"]
        user_repository = environment["user_repository"]

        request_result = service.request_password_reset("estudiante@lasalle.edu.co")
        self.assertTrue(request_result.success)
        self.assertEqual(len(notifier.sent_messages), 1)

        token = notifier.sent_messages[0].metadata["token"]
        reset_result = service.reset_password(
            email="estudiante@lasalle.edu.co",
            token=token,
            new_password="NuevaClaveSegura123!",
        )

        self.assertTrue(reset_result.success)
        updated_user = user_repository.find_by_email("estudiante@lasalle.edu.co")
        self.assertEqual(updated_user.password_hash, hash_password("NuevaClaveSegura123!"))

    def test_reset_fails_when_password_is_weak(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        notifier = environment["notifier"]

        service.request_password_reset("estudiante@lasalle.edu.co")
        token = notifier.sent_messages[0].metadata["token"]

        reset_result = service.reset_password(
            email="estudiante@lasalle.edu.co",
            token=token,
            new_password="debil",
        )

        self.assertFalse(reset_result.success)
        self.assertIn("contrasena", reset_result.message.lower())


if __name__ == "__main__":
    unittest.main()
