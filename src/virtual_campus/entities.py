from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class User:
    email: str
    password_hash: str
    active: bool = True


@dataclass
class ResetToken:
    email: str
    token: str
    expires_at: datetime
    used: bool = False

    def is_expired(self, now: datetime) -> bool:
        return now >= self.expires_at


@dataclass
class NotificationMessage:
    recipient: str
    subject: str
    body: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AuditEvent:
    event_name: str
    email: str
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ServiceResult:
    success: bool
    message: str
