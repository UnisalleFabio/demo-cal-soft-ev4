# Metricas y seguimiento del ejemplo

## Metricas sugeridas

| Metrica | Como se interpreta en este ejemplo |
|---|---|
| Cobertura de pruebas | Cuanto del flujo de recuperacion esta cubierto por pruebas unitarias, funcionales e integradas |
| Tasa de exito | Cuantos casos del modulo pasan y cuantos fallan |
| Severidad | Que tan critico seria un defecto en recuperacion de contrasena |
| Trazabilidad | Si cada funcionalidad del flujo tiene pruebas y hallazgos asociados |

## Evidencias observables

- mensajes enviados por `InMemoryNotificationService`;
- eventos registrados en `InMemoryAuditLog`;
- token almacenado en `InMemoryResetTokenRepository`;
- resultados de las pruebas automatizadas;
- issues de ejemplo en `quality/github-issues/`;
- pipeline definido en `.github/workflows/ci.yml`.

## Seguimiento de hallazgos de ejemplo

| ID | Hallazgo | Severidad | Estado | Evidencia | Caso asociado |
|---|---|---|---|---|---|
| INC-01 | El mensaje de correo no incluye fecha de expiracion del token | Media | Pendiente | `quality/github-issues/INC-01-fecha-expiracion.md` | `F-02` |
| INC-02 | No existe limitacion de intentos fallidos de restablecimiento | Alta | En analisis | `quality/github-issues/INC-02-intentos-fallidos.md` | `I-02` |
| INC-03 | No se notifica al usuario cuando el token ya fue usado | Baja | Pendiente | `quality/github-issues/INC-03-token-usado.md` | `F-03` |
