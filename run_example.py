from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from virtual_campus.app import build_demo_environment


def main() -> None:
    environment = build_demo_environment()
    service = environment["service"]
    notifier = environment["notifier"]
    audit_log = environment["audit_log"]

    print("== Solicitud de recuperacion ==")
    request_result = service.request_password_reset("estudiante@lasalle.edu.co")
    print(request_result.message)

    latest_notification = notifier.sent_messages[-1]
    token = latest_notification.metadata["token"]

    print("\n== Restablecimiento de contrasena ==")
    reset_result = service.reset_password(
        email="estudiante@lasalle.edu.co",
        token=token,
        new_password="NuevaClaveSegura123!",
    )
    print(reset_result.message)

    print("\n== Eventos de auditoria ==")
    for event in audit_log.events:
        print(f"- {event.event_name} | {event.email}")


if __name__ == "__main__":
    main()
