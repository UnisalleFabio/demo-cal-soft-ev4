from .entities import AuditEvent


class InMemoryAuditLog:
    def __init__(self) -> None:
        self.events: list[AuditEvent] = []

    def record(self, event_name: str, email: str, **details) -> None:
        self.events.append(
            AuditEvent(
                event_name=event_name,
                email=email,
                details=details,
            )
        )
