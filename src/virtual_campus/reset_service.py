from .audit import InMemoryAuditLog
from .entities import ServiceResult
from .notifier import InMemoryNotificationService
from .password_policy import PasswordPolicy, PasswordPolicyError
from .repositories import InMemoryResetTokenRepository, InMemoryUserRepository
from .security import hash_password
from .token_service import TokenService


GENERIC_RESET_MESSAGE = (
    "Si el correo existe y esta activo, recibiras instrucciones para recuperar tu contrasena."
)


class PasswordResetService:
    def __init__(
        self,
        user_repository: InMemoryUserRepository,
        token_repository: InMemoryResetTokenRepository,
        token_service: TokenService,
        notification_service: InMemoryNotificationService,
        audit_log: InMemoryAuditLog,
        password_policy: PasswordPolicy,
    ) -> None:
        self.user_repository = user_repository
        self.token_repository = token_repository
        self.token_service = token_service
        self.notification_service = notification_service
        self.audit_log = audit_log
        self.password_policy = password_policy

    def request_password_reset(self, email: str) -> ServiceResult:
        user = self.user_repository.find_by_email(email)
        if user is None or not user.active:
            self.audit_log.record("password_reset_request_ignored", email)
            return ServiceResult(success=True, message=GENERIC_RESET_MESSAGE)

        reset_token = self.token_service.generate(email)
        self.token_repository.save(reset_token)
        self.notification_service.send_password_reset_email(email, reset_token.token)
        self.audit_log.record(
            "password_reset_requested",
            email,
            expires_at=reset_token.expires_at.isoformat(),
        )
        return ServiceResult(success=True, message=GENERIC_RESET_MESSAGE)

    def reset_password(self, email: str, token: str, new_password: str) -> ServiceResult:
        user = self.user_repository.find_by_email(email)
        if user is None or not user.active:
            self.audit_log.record("password_reset_failed_unknown_user", email)
            return ServiceResult(success=False, message="No fue posible restablecer la contrasena.")

        stored_token = self.token_repository.find_by_email(email)
        if not self.token_service.is_valid(stored_token, token):
            self.audit_log.record("password_reset_failed_invalid_token", email)
            return ServiceResult(success=False, message="El token es invalido o ya expiro.")

        try:
            self.password_policy.validate(new_password)
        except PasswordPolicyError as exc:
            self.audit_log.record("password_reset_failed_policy", email, error=str(exc))
            return ServiceResult(success=False, message=str(exc))

        self.user_repository.update_password(email, hash_password(new_password))
        self.token_repository.mark_used(email)
        self.audit_log.record("password_reset_completed", email)
        return ServiceResult(
            success=True,
            message="La contrasena fue restablecida correctamente.",
        )
