# INC-03 - El usuario no recibe aviso cuando el token ya fue usado

- Estado: `Open`
- Tipo: `test-gap`
- Severidad: `baja`
- Modulo: `token_service`
- Caso asociado: `F-03`

## Descripcion

El sistema rechaza el token reutilizado, pero no comunica con suficiente claridad que el enlace ya fue consumido.

## Resultado esperado

El usuario debe recibir un mensaje claro indicando que debe solicitar un nuevo enlace.

## Resultado actual

La operacion falla sin un mensaje suficientemente orientador.

## Impacto

- genera confusion;
- reduce usabilidad;
- puede aumentar tickets de soporte.

## Evidencia

- `src/virtual_campus/token_service.py`
- `tests/test_functional_password_reset.py`

