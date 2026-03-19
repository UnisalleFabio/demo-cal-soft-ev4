from datetime import datetime, timedelta
import unittest

from _helpers import ROOT  # noqa: F401
from virtual_campus.entities import ResetToken
from virtual_campus.token_service import TokenService


class TokenServiceTests(unittest.TestCase):
    def test_generated_token_has_future_expiration(self) -> None:
        now = datetime(2026, 2, 28, 10, 0, 0)
        service = TokenService(now_fn=lambda: now)

        reset_token = service.generate("estudiante@lasalle.edu.co")

        self.assertEqual(reset_token.email, "estudiante@lasalle.edu.co")
        self.assertGreater(reset_token.expires_at, now)

    def test_rejects_expired_token(self) -> None:
        now = datetime(2026, 2, 28, 10, 0, 0)
        service = TokenService(now_fn=lambda: now)
        expired = ResetToken(
            email="estudiante@lasalle.edu.co",
            token="abc123",
            expires_at=now - timedelta(minutes=1),
        )

        self.assertFalse(service.is_valid(expired, "abc123"))

    def test_rejects_already_used_token(self) -> None:
        now = datetime(2026, 2, 28, 10, 0, 0)
        service = TokenService(now_fn=lambda: now)
        used = ResetToken(
            email="estudiante@lasalle.edu.co",
            token="abc123",
            expires_at=now + timedelta(minutes=10),
            used=True,
        )

        self.assertTrue(service.is_valid(used, "abc123"))


if __name__ == "__main__":
    unittest.main()
