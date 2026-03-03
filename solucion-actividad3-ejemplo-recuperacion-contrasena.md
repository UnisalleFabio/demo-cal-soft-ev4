# Solución ejemplo de la Actividad 3

## Plan de pruebas unitarias y funcionales

> Documento de referencia construido a partir del proyecto `ejemplo-recuperacion-contrasena`
> Su objetivo es mostrar cómo se vería un entregable completo y coherente para la [actividad3.md](actividad3.md)

## 1. Datos generales

| Campo | Información |
|---|---|
| Asignatura | Calidad de Software I |
| Actividad | Actividad 3. Diseñemos y ejecutemos las pruebas de software |
| Integrantes del grupo | Equipo de ejemplo docente |
| Software o sistema seleccionado | Aula virtual - módulo de recuperación de contraseña |
| Versión o entorno probado | Ejecución local con Python 3.12 y repositorios en memoria |
| Fecha de elaboración y ejecución | 28 de febrero de 2026 |

## 2. Descripción del software

El sistema evaluado corresponde a un módulo de recuperación de contraseña para un aula virtual. Su objetivo es permitir que un estudiante solicite el restablecimiento de su clave, reciba un token temporal y actualice su contraseña de manera controlada.

Aunque el ejemplo es pequeño, representa un proceso sensible dentro de un sistema académico real porque involucra:

- acceso a cuentas de usuario
- reglas de seguridad para la nueva contraseña
- generación y validación de tokens
- notificaciones al usuario
- auditoría de eventos relevantes

## 3. Componentes o módulos principales

| Componente o módulo | Archivo principal | Descripción |
|---|---|---|
| Configuración del entorno | `src/virtual_campus/app.py` | Construye el entorno demo y registra un usuario inicial |
| Servicio de recuperación | `src/virtual_campus/reset_service.py` | Coordina solicitud, validación y restablecimiento |
| Política de contraseñas | `src/virtual_campus/password_policy.py` | Valida reglas mínimas de seguridad |
| Servicio de tokens | `src/virtual_campus/token_service.py` | Genera tokens y verifica expiración o reuso |
| Repositorios en memoria | `src/virtual_campus/repositories.py` | Guarda usuarios y tokens durante la ejecución |
| Notificación | `src/virtual_campus/notifier.py` | Simula el envío del mensaje de recuperación |
| Auditoría | `src/virtual_campus/audit.py` | Registra eventos del flujo |

## 4. Alcance del plan de pruebas

### Qué se prueba

- reglas de validación de contraseña
- generación y validación de tokens
- flujo funcional de solicitud de recuperación
- flujo funcional de restablecimiento de contraseña
- comportamiento del sistema ante escenarios negativos
- evidencia de auditoría y notificación

### Qué no se prueba

- interfaz web real
- integración con una base de datos persistente
- envío real de correos por SMTP
- autenticación completa del aula virtual fuera del módulo de recuperación

### Supuestos del entorno

- el módulo se ejecuta localmente
- existe un usuario activo precargado: `estudiante@lasalle.edu.co`
- el token tiene vigencia configurada por defecto a 15 minutos
- los resultados reales se obtuvieron ejecutando pruebas automatizadas y verificaciones manuales locales

### Riesgos o limitaciones

- al no existir interfaz web, algunos hallazgos se validan por inspección del mensaje o del resultado del servicio
- los repositorios en memoria simplifican el comportamiento frente a concurrencia y persistencia
- la cobertura del ejemplo se concentra en el módulo de recuperación, no en todo un LMS real

## 5. Inventario de funcionalidades

Se identificaron 20 funcionalidades del módulo. En esta iteración se ejecutaron pruebas prioritarias sobre 12 de ellas.

| ID | Módulo | Funcionalidad | Tipo principal de prueba | Prioridad | Estado |
|---|---|---|---|---|---|
| FN-01 | Usuarios | Buscar usuario por correo | Funcional | Alta | Ejecutada |
| FN-02 | Usuarios | Verificar que el usuario esté activo | Funcional | Alta | Ejecutada |
| FN-03 | Tokens | Generar token aleatorio | Unitaria | Alta | Ejecutada |
| FN-04 | Tokens | Definir expiración del token | Unitaria | Alta | Ejecutada |
| FN-05 | Tokens | Guardar token asociado al correo | Funcional | Alta | Ejecutada |
| FN-06 | Notificación | Generar mensaje de recuperación | Funcional | Alta | Ejecutada |
| FN-07 | Notificación | Asociar token al mensaje enviado | Funcional | Alta | Ejecutada |
| FN-08 | Solicitud | Responder con mensaje genérico al solicitante | Funcional | Alta | Ejecutada |
| FN-09 | Auditoría | Registrar solicitud ignorada para usuario inexistente o inactivo | Funcional | Media | Ejecutada |
| FN-10 | Auditoría | Registrar solicitud válida con fecha de expiración | Funcional | Alta | Ejecutada |
| FN-11 | Restablecimiento | Validar existencia y estado del usuario al restablecer | Funcional | Alta | Ejecutada |
| FN-12 | Restablecimiento | Validar coincidencia del token recibido | Funcional | Alta | Ejecutada |
| FN-13 | Restablecimiento | Rechazar token expirado | Unitaria | Alta | Ejecutada |
| FN-14 | Restablecimiento | Rechazar token ya utilizado | Unitaria | Alta | Ejecutada |
| FN-15 | Seguridad | Validar longitud mínima de contraseña | Unitaria | Alta | Ejecutada |
| FN-16 | Seguridad | Validar presencia de letra minúscula | Unitaria | Media | Pendiente |
| FN-17 | Seguridad | Validar presencia de letra mayúscula | Unitaria | Alta | Ejecutada |
| FN-18 | Seguridad | Validar presencia de número | Unitaria | Media | Pendiente |
| FN-19 | Seguridad | Validar presencia de carácter especial | Unitaria | Alta | Ejecutada |
| FN-20 | Restablecimiento | Actualizar contraseña, marcar token usado y registrar auditoría final | Funcional | Alta | Ejecutada |

## 6. Estrategia de ejecución

Se ejecutaron dos grupos de pruebas:

- 10 pruebas automatizadas existentes en la carpeta `tests/`
- 2 verificaciones funcionales manuales complementarias para revisar mensajes y usabilidad del flujo

Comando usado para la suite automatizada:

```bash
cd calidad-software-I/ev4/ejemplo-recuperacion-contrasena
python3 -m unittest discover -s tests -v
```

Resultado global de la suite automatizada:

- 10 pruebas ejecutadas
- 10 pruebas aprobadas
- 0 fallos en la automatización

Resultado global del plan presentado en este documento:

- 12 casos ejecutados
- 10 casos aprobados
- 2 casos fallidos
- tasa de éxito general: `83.3%`

## 7. Casos de prueba unitarios

### Caso unitario U-01

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-15, FN-16, FN-17, FN-18, FN-19 |
| Descripción del caso de prueba | Verificar que la política acepte una contraseña fuerte |
| Precondiciones | Política de contraseña cargada con longitud mínima de 10 |
| Datos de entrada | `ClaveSegura123!` |
| Pasos a seguir | 1. Instanciar `PasswordPolicy(min_length=10)`. 2. Ejecutar `validate("ClaveSegura123!")`. |
| Resultado esperado | La validación termina sin lanzar excepción |
| Resultado real | La validación terminó sin excepción |
| Posibles errores identificados | Ninguno |
| Mejoras propuestas | Mantener este caso en regresión |
| Evidencia | `tests/test_unit_password_policy.py::test_accepts_a_strong_password` |

### Caso unitario U-02

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-17 |
| Descripción del caso de prueba | Verificar que la política rechace una contraseña sin mayúscula |
| Precondiciones | Política de contraseña cargada con longitud mínima de 10 |
| Datos de entrada | `clavesegura123!` |
| Pasos a seguir | 1. Instanciar la política. 2. Ejecutar `validate("clavesegura123!")`. |
| Resultado esperado | Se genera una excepción de política por ausencia de mayúscula |
| Resultado real | Se generó `PasswordPolicyError` como se esperaba |
| Posibles errores identificados | Ninguno |
| Mejoras propuestas | Agregar también el caso negativo por falta de minúscula |
| Evidencia | `tests/test_unit_password_policy.py::test_rejects_password_without_uppercase` |

### Caso unitario U-03

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-19 |
| Descripción del caso de prueba | Verificar que la política rechace una contraseña sin carácter especial |
| Precondiciones | Política de contraseña cargada con longitud mínima de 10 |
| Datos de entrada | `ClaveSegura123` |
| Pasos a seguir | 1. Instanciar la política. 2. Ejecutar `validate("ClaveSegura123")`. |
| Resultado esperado | Se genera una excepción de política por ausencia de carácter especial |
| Resultado real | Se generó `PasswordPolicyError` como se esperaba |
| Posibles errores identificados | Ninguno |
| Mejoras propuestas | Agregar pruebas negativas por falta de número y minúscula |
| Evidencia | `tests/test_unit_password_policy.py::test_rejects_password_without_special_character` |

### Caso unitario U-04

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-03, FN-04 |
| Descripción del caso de prueba | Verificar que el token generado tenga expiración futura |
| Precondiciones | `TokenService` configurado con tiempo actual fijo `2026-02-28 10:00:00` |
| Datos de entrada | `estudiante@lasalle.edu.co` |
| Pasos a seguir | 1. Instanciar `TokenService(now_fn=lambda: now)`. 2. Ejecutar `generate(email)`. |
| Resultado esperado | El token queda asociado al correo y su expiración es posterior a `now` |
| Resultado real | Se generó un token para `estudiante@lasalle.edu.co` con expiración futura y el test confirma que `expires_at > now` |
| Posibles errores identificados | Ninguno |
| Mejoras propuestas | Registrar visualmente la vigencia del token en la notificación al usuario |
| Evidencia | `tests/test_unit_token_service.py::test_generated_token_has_future_expiration` |

### Caso unitario U-05

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-13 |
| Descripción del caso de prueba | Verificar que un token expirado sea rechazado |
| Precondiciones | `TokenService` con tiempo actual fijo y un `ResetToken` vencido |
| Datos de entrada | Token `abc123` expirado |
| Pasos a seguir | 1. Construir `ResetToken` con expiración anterior al tiempo actual. 2. Ejecutar `is_valid(expired, "abc123")`. |
| Resultado esperado | La validación retorna `False` |
| Resultado real | La validación retornó `False` |
| Posibles errores identificados | Ninguno |
| Mejoras propuestas | Agregar un mensaje funcional que explique al usuario que debe solicitar un nuevo enlace |
| Evidencia | `tests/test_unit_token_service.py::test_rejects_expired_token` |

### Caso unitario U-06

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-14 |
| Descripción del caso de prueba | Verificar que un token marcado como usado sea rechazado |
| Precondiciones | `TokenService` con un `ResetToken` vigente pero `used=True` |
| Datos de entrada | Token `abc123` ya utilizado |
| Pasos a seguir | 1. Construir `ResetToken` válido y usado. 2. Ejecutar `is_valid(used, "abc123")`. |
| Resultado esperado | La validación retorna `False` |
| Resultado real | La validación retornó `False` |
| Posibles errores identificados | Ninguno a nivel técnico |
| Mejoras propuestas | Complementar con un mensaje funcional más claro para el usuario final |
| Evidencia | `tests/test_unit_token_service.py::test_rejects_already_used_token` |

## 8. Casos de prueba funcionales

### Caso funcional F-01

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-01, FN-02, FN-03, FN-05, FN-06, FN-07, FN-08, FN-10 |
| Descripción del caso de prueba | Verificar que un usuario activo pueda solicitar recuperación de contraseña y reciba una notificación |
| Precondiciones | Usuario `estudiante@lasalle.edu.co` activo en el repositorio |
| Datos de entrada | Correo `estudiante@lasalle.edu.co` |
| Pasos a seguir | 1. Construir el entorno demo. 2. Ejecutar `request_password_reset(email)`. 3. Revisar mensajes enviados. |
| Resultado esperado | El sistema responde éxito, guarda token y envía un mensaje |
| Resultado real | `success=True`, se envió 1 mensaje y se generó el mensaje genérico de recuperación |
| Posibles errores identificados | Ninguno en el flujo básico |
| Mejoras propuestas | Mostrar al usuario información adicional sobre vigencia del enlace |
| Evidencia | `tests/test_functional_password_reset.py::test_user_can_request_and_reset_password` |

### Caso funcional F-02

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-11, FN-12, FN-20 |
| Descripción del caso de prueba | Verificar que un usuario pueda restablecer la contraseña con un token válido |
| Precondiciones | Usuario activo y solicitud de recuperación ya ejecutada |
| Datos de entrada | Correo `estudiante@lasalle.edu.co`, token emitido por el sistema, nueva contraseña `NuevaClaveSegura123!` |
| Pasos a seguir | 1. Solicitar recuperación. 2. Obtener token desde la notificación. 3. Ejecutar `reset_password(...)`. 4. Revisar hash de la contraseña. |
| Resultado esperado | La operación termina con éxito, se actualiza la contraseña y el token queda inutilizable |
| Resultado real | `success=True`, el hash del usuario cambió y el flujo concluyó correctamente |
| Posibles errores identificados | Ninguno en el escenario exitoso |
| Mejoras propuestas | Agregar confirmación visible de expiración y de un solo uso del enlace |
| Evidencia | `tests/test_functional_password_reset.py::test_user_can_request_and_reset_password` y `tests/test_integration_password_reset_service.py::test_reset_password_marks_token_as_used_and_records_audit` |

### Caso funcional F-03

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-15 |
| Descripción del caso de prueba | Verificar que el restablecimiento falle cuando la nueva contraseña es débil |
| Precondiciones | Usuario activo, token válido emitido previamente |
| Datos de entrada | Nueva contraseña `debil` |
| Pasos a seguir | 1. Solicitar recuperación. 2. Obtener token. 3. Ejecutar `reset_password(...)` con una clave débil. |
| Resultado esperado | El sistema rechaza la operación y explica la razón |
| Resultado real | `success=False` y mensaje real: `La contrasena debe tener al menos 10 caracteres.` |
| Posibles errores identificados | Ninguno, el control funciona como se espera |
| Mejoras propuestas | Agregar mensajes preventivos en interfaz antes de enviar la solicitud |
| Evidencia | `tests/test_functional_password_reset.py::test_reset_fails_when_password_is_weak` |

### Caso funcional F-04

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-01, FN-08, FN-09 |
| Descripción del caso de prueba | Verificar que el sistema no revele si un correo inexistente pertenece o no a un usuario válido |
| Precondiciones | No existe el usuario `desconocido@lasalle.edu.co` |
| Datos de entrada | Correo `desconocido@lasalle.edu.co` |
| Pasos a seguir | 1. Construir el entorno demo. 2. Ejecutar `request_password_reset("desconocido@lasalle.edu.co")`. 3. Revisar mensajes enviados y evento de auditoría. |
| Resultado esperado | El sistema retorna mensaje genérico, no envía correo y registra la solicitud ignorada |
| Resultado real | `success=True`, mensaje real `Si el correo existe y esta activo, recibiras instrucciones para recuperar tu contrasena.`, `0` mensajes enviados y auditoría `password_reset_request_ignored` |
| Posibles errores identificados | Ninguno, el flujo protege contra enumeración de usuarios |
| Mejoras propuestas | Mantener este comportamiento como requisito no funcional de seguridad |
| Evidencia | Ejecución manual local del 28 de febrero de 2026 sobre `virtual_campus.app.build_demo_environment()` |

### Caso funcional F-05

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-06 |
| Descripción del caso de prueba | Verificar que el mensaje enviado informe la vigencia o expiración del token |
| Precondiciones | Usuario activo y solicitud de recuperación disponible |
| Datos de entrada | Correo `estudiante@lasalle.edu.co` |
| Pasos a seguir | 1. Solicitar recuperación. 2. Revisar el cuerpo del mensaje generado por `InMemoryNotificationService`. |
| Resultado esperado | El mensaje informa que el enlace o token expira en un tiempo definido |
| Resultado real | El cuerpo real fue: `Se genero una solicitud para recuperar la contrasena. Usa el token recibido para continuar el proceso.` No informa expiración |
| Posibles errores identificados | Hallazgo funcional `INC-01`: falta de información de vigencia para el usuario |
| Mejoras propuestas | Incluir expiración visible en el cuerpo del mensaje y, si es posible, en metadatos del correo |
| Evidencia | Ejecución manual local del 28 de febrero de 2026 y `quality/github-issues/INC-01-fecha-expiracion.md` |

### Caso funcional F-06

| Campo | Detalle |
|---|---|
| Funcionalidad asociada | FN-14, FN-20 |
| Descripción del caso de prueba | Verificar que el sistema oriente claramente al usuario cuando intenta reutilizar un token ya consumido |
| Precondiciones | Usuario activo, token emitido y ya usado en un restablecimiento exitoso |
| Datos de entrada | Mismo token reutilizado después de un restablecimiento válido |
| Pasos a seguir | 1. Solicitar recuperación. 2. Restablecer la contraseña con éxito. 3. Reutilizar el mismo token en un segundo intento. |
| Resultado esperado | El sistema rechaza el segundo uso y orienta al usuario a solicitar un nuevo enlace |
| Resultado real | `success=False` y mensaje real: `El token es invalido o ya expiro.` El rechazo funciona, pero el mensaje no aclara si el token fue usado o expirado |
| Posibles errores identificados | Hallazgo funcional `INC-03`: mensaje poco específico para un caso frecuente de reuso |
| Mejoras propuestas | Diferenciar mensaje de token expirado y token ya usado, e invitar a solicitar un nuevo enlace |
| Evidencia | Ejecución manual local del 28 de febrero de 2026 y `quality/github-issues/INC-03-token-usado.md` |

## 9. Registro resumido de ejecución

| ID del caso | Tipo | Estado | Resultado esperado cumplido | Error encontrado | Mejora sugerida |
|---|---|---|---|---|---|
| U-01 | Unitario | Aprobado | Sí | No | Mantener en regresión |
| U-02 | Unitario | Aprobado | Sí | No | Agregar caso por falta de minúscula |
| U-03 | Unitario | Aprobado | Sí | No | Agregar caso por falta de número |
| U-04 | Unitario | Aprobado | Sí | No | Mostrar expiración al usuario |
| U-05 | Unitario | Aprobado | Sí | No | Mejorar mensaje funcional |
| U-06 | Unitario | Aprobado | Sí | No | Diferenciar mensaje de reuso |
| F-01 | Funcional | Aprobado | Sí | No | Informar vigencia del enlace |
| F-02 | Funcional | Aprobado | Sí | No | Mostrar confirmación adicional |
| F-03 | Funcional | Aprobado | Sí | No | Agregar ayuda preventiva en UI |
| F-04 | Funcional | Aprobado | Sí | No | Mantener como control de seguridad |
| F-05 | Funcional | Fallido | No | Sí, `INC-01` | Incluir expiración en el mensaje |
| F-06 | Funcional | Fallido | No | Sí, `INC-03` | Hacer mensaje más específico |

## 10. Hallazgos consolidados

| ID | Hallazgo | Severidad | Evidencia | Recomendación |
|---|---|---|---|---|
| H-01 | El mensaje de recuperación no informa la expiración del token | Media | `quality/github-issues/INC-01-fecha-expiracion.md` | Actualizar `notifier.py` para incluir la vigencia |
| H-02 | No existe limitación de intentos fallidos de restablecimiento | Alta | `quality/github-issues/INC-02-intentos-fallidos.md` | Incorporar contador de intentos y bloqueo temporal |
| H-03 | El mensaje para token reutilizado no orienta con claridad al usuario | Baja | `quality/github-issues/INC-03-token-usado.md` | Diferenciar mensajes para expiración y reuso |

## 11. Conclusiones

El módulo presenta una base funcional correcta para el flujo principal de recuperación de contraseña. Las pruebas unitarias y funcionales ejecutadas muestran que la lógica central de validación, generación de token y cambio de contraseña funciona de forma estable en los escenarios cubiertos.

Sin embargo, los principales hallazgos no están en la mecánica básica del flujo sino en la calidad de la experiencia y en controles adicionales de seguridad. Los dos problemas más relevantes para priorizar son:

- la falta de información visible sobre la expiración del enlace
- la ausencia de limitación de intentos fallidos durante el restablecimiento

Como resultado, el nivel de calidad observado es aceptable para fines de demostración académica, pero todavía requiere mejoras antes de considerarse un flujo robusto para un entorno real.

## 12. Lista de chequeo final

- Se seleccionó un sistema de software con descripción clara
- Se identificaron 20 funcionalidades del módulo evaluado
- Se documentaron componentes principales
- Se diseñaron casos unitarios y funcionales
- Cada caso incluye descripción, pasos, resultado esperado y resultado real
- Los resultados reales provienen de ejecución automatizada o verificaciones manuales locales
- Se documentaron errores y mejoras
- Se mantuvo coherencia entre funcionalidades, casos y hallazgos
- No se usaron resultados inventados ni evidencia ficticia

## 13. Evidencias complementarias

- Código fuente: `calidad-software-I/ev4/ejemplo-recuperacion-contrasena/src/virtual_campus/`
- Suite automatizada: `calidad-software-I/ev4/ejemplo-recuperacion-contrasena/tests/`
- Seguimiento de hallazgos: `calidad-software-I/ev4/ejemplo-recuperacion-contrasena/quality/github-issues/`
- Gestión formal de pruebas: `calidad-software-I/ev4/ejemplo-recuperacion-contrasena/quality/test-management/`
- Mejora continua: `calidad-software-I/ev4/ejemplo-recuperacion-contrasena/quality/plan-mejora-continua.md`
