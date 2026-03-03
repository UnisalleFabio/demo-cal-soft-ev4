import unittest

from _helpers import ROOT  # noqa: F401
from virtual_campus.app import build_demo_environment


class PasswordResetIntegrationTests(unittest.TestCase):
    def test_request_password_reset_persists_token_sends_email_and_records_audit(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        token_repository = environment["token_repository"]
        notifier = environment["notifier"]
        audit_log = environment["audit_log"]

        service.request_password_reset("estudiante@lasalle.edu.co")

        stored_token = token_repository.find_by_email("estudiante@lasalle.edu.co")
        self.assertIsNotNone(stored_token)
        self.assertEqual(len(notifier.sent_messages), 1)
        self.assertEqual(audit_log.events[-1].event_name, "password_reset_requested")

    def test_reset_password_marks_token_as_used_and_records_audit(self) -> None:
        environment = build_demo_environment()
        service = environment["service"]
        token_repository = environment["token_repository"]
        notifier = environment["notifier"]
        audit_log = environment["audit_log"]

        service.request_password_reset("estudiante@lasalle.edu.co")
        token = notifier.sent_messages[0].metadata["token"]
        result = service.reset_password(
            email="estudiante@lasalle.edu.co",
            token=token,
            new_password="NuevaClaveSegura123!",
        )

        self.assertTrue(result.success)
        self.assertTrue(
            token_repository.find_by_email("estudiante@lasalle.edu.co").used
        )
        self.assertEqual(audit_log.events[-1].event_name, "password_reset_completed")


if __name__ == "__main__":
    unittest.main()
