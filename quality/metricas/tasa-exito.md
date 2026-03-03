# Tasa de Éxito de Pruebas

Guía para medir la tasa de éxito (pass rate) de las pruebas automatizadas del
proyecto **ejemplo-recuperacion-contraseña**.

> Todos los comandos se ejecutan desde la **raíz del repositorio**.

## Requisitos previos

```bash
py -3.13 -m pip install pytest
```

> El proyecto requiere **Python 3.11+** porque utiliza `datetime.UTC`,
> introducido en esa versión.

## Ejecutar todas las pruebas

```bash
py -3.13 -m pytest tests/ -v
```

La salida muestra cada prueba con su resultado y un porcentaje de progreso:

```
tests/test_unit_password_policy.py::test_min_length PASSED       [ 10%]
tests/test_unit_password_policy.py::test_uppercase  PASSED       [ 20%]
...
========================= 10 passed in 0.05s =========================
```

## Cómo calcular la tasa de éxito

```
Tasa de éxito = (pruebas pasadas / pruebas totales) × 100
```

| Escenario | Resultado | Tasa |
|-----------|-----------|------|
| 10 pasadas, 0 fallidas | `10 passed` | 100% |
| 8 pasadas, 2 fallidas | `8 passed, 2 failed` | 80% |
| 9 pasadas, 1 error | `9 passed, 1 error` | 90% |

## Ejecutar por nivel de prueba

### Solo pruebas unitarias

```bash
py -3.13 -m pytest tests/test_unit_password_policy.py tests/test_unit_token_service.py -v
```

### Solo pruebas de integración

```bash
py -3.13 -m pytest tests/test_integration_password_reset_service.py -v
```

### Solo pruebas funcionales

```bash
py -3.13 -m pytest tests/test_functional_password_reset.py -v
```

## Alternativa con unittest (sin instalar pytest)

```bash
py -3.13 -m unittest discover -s tests -v
```

`unittest` no muestra porcentaje, pero el resumen final indica el total de
pruebas ejecutadas y los fallos:

```
Ran 10 tests in 0.032s

OK
```

Si hay fallos:

```
Ran 10 tests in 0.045s

FAILED (failures=2)
```