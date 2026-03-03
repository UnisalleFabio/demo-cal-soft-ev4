from datetime import UTC, datetime, timedelta
import secrets

from .entities import ResetToken


class TokenService:
    def __init__(
        self,
        ttl_minutes: int = 15,
        now_fn=None,
    ) -> None:
        self.ttl_minutes = ttl_minutes
        self.now_fn = now_fn or (lambda: datetime.now(UTC))

    def generate(self, email: str) -> ResetToken:
        now = self.now_fn()
        token = secrets.token_urlsafe(16)
        return ResetToken(
            email=email,
            token=token,
            expires_at=now + timedelta(minutes=self.ttl_minutes),
        )

    def is_valid(self, reset_token: ResetToken | None, provided_token: str) -> bool:
        if reset_token is None:
            return False
        if reset_token.used:
            return False
        if reset_token.token != provided_token:
            return False
        if reset_token.is_expired(self.now_fn()):
            return False
        return True
