from .audit import InMemoryAuditLog
from .entities import User
from .notifier import InMemoryNotificationService
from .password_policy import PasswordPolicy
from .repositories import InMemoryResetTokenRepository, InMemoryUserRepository
from .reset_service import PasswordResetService
from .security import hash_password
from .token_service import TokenService


def build_demo_environment(now_fn=None) -> dict[str, object]:
    user_repository = InMemoryUserRepository()
    token_repository = InMemoryResetTokenRepository()
    notification_service = InMemoryNotificationService()
    audit_log = InMemoryAuditLog()
    password_policy = PasswordPolicy()
    token_service = TokenService(now_fn=now_fn)

    user_repository.save(
        User(
            email="estudiantes@lasalle.edu.co",
            password_hash=hash_password("ClaveInicial123!"),
        )
    )

    service = PasswordResetService(
        user_repository=user_repository,
        token_repository=token_repository,
        token_service=token_service,
        notification_service=notification_service,
        audit_log=audit_log,
        password_policy=password_policy,
    )

    return {
        "service": service,
        "user_repository": user_repository,
        "token_repository": token_repository,
        "notifier": notification_service,
        "audit_log": audit_log,
    }
