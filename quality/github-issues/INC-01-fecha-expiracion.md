# INC-01 - El correo no informa la expiracion del token

- Estado: `Open`
- Tipo: `bug`
- Severidad: `media`
- Modulo: `notifier`
- Caso asociado: `F-02`

## Descripcion

El correo de recuperacion entrega el enlace, pero no comunica al usuario hasta cuando es valido el token.

## Resultado esperado

El mensaje debe indicar que el enlace expira en un tiempo definido.

## Resultado actual

El correo solo incluye el enlace.

## Impacto

- aumenta consultas al soporte;
- reduce claridad del flujo;
- debilita la experiencia de usuario.

## Evidencia

- `src/virtual_campus/notifier.py`
- `tests/test_functional_password_reset.py`

