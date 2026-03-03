from .entities import ResetToken, User


class InMemoryUserRepository:
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def save(self, user: User) -> None:
        self._users[user.email] = user

    def find_by_email(self, email: str) -> User | None:
        return self._users.get(email)

    def update_password(self, email: str, new_password_hash: str) -> None:
        user = self._users[email]
        self._users[email] = User(
            email=user.email,
            password_hash=new_password_hash,
            active=user.active,
        )


class InMemoryResetTokenRepository:
    def __init__(self) -> None:
        self._tokens: dict[str, ResetToken] = {}

    def save(self, reset_token: ResetToken) -> None:
        self._tokens[reset_token.email] = reset_token

    def find_by_email(self, email: str) -> ResetToken | None:
        return self._tokens.get(email)

    def mark_used(self, email: str) -> None:
        token = self._tokens[email]
        token.used = True
