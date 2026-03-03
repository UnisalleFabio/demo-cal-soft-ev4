from .entities import NotificationMessage


class InMemoryNotificationService:
    def __init__(self) -> None:
        self.sent_messages: list[NotificationMessage] = []

    def send_password_reset_email(self, email: str, token: str) -> None:
        message = NotificationMessage(
            recipient=email,
            subject="Recuperacion de contrasena",
            body=(
                "Se genero una solicitud para recuperar la contrasena. "
                "Usa el token recibido para continuar el proceso."
            ),
            metadata={"token": token},
        )
        self.sent_messages.append(message)
