# INC-02 - No existe limitacion de intentos fallidos

- Estado: `Open`
- Tipo: `bug`
- Severidad: `alta`
- Modulo: `reset_service`
- Caso asociado: `I-02`

## Descripcion

El flujo de restablecimiento no restringe intentos fallidos repetidos al ingresar una nueva contrasena.

## Resultado esperado

Despues de un numero definido de intentos fallidos, el sistema debe bloquear temporalmente la operacion o invalidar el token.

## Resultado actual

El usuario puede repetir intentos fallidos sin limitacion.

## Impacto

- incrementa el riesgo de abuso del flujo;
- dificulta auditoria de comportamiento sospechoso;
- expone una debilidad de seguridad.

## Evidencia

- `src/virtual_campus/reset_service.py`
- `tests/test_integration_password_reset_service.py`

