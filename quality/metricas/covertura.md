# Cobertura de Código

Guía para medir la cobertura de las pruebas automatizadas del proyecto
**ejemplo-recuperacion-contraseña** usando [`coverage.py`](https://coverage.readthedocs.io/).

> Todos los comandos se ejecutan desde la **raíz del repositorio**.

## Requisitos previos

```bash
python3 -m pip install --upgrade pip coverage
```

## Ejecutar todas las pruebas con cobertura

```bash
coverage run -m unittest discover -s tests -v
coverage report -m
```

| Flag | Descripción |
|------|-------------|
| `-v` | Salida detallada (verbose) |
| `-m` | Muestra las líneas no cubiertas en el reporte |

## Ejecutar solo pruebas unitarias

Si deseas excluir las pruebas funcionales e integradas y medir cobertura
únicamente de las pruebas unitarias:

```bash
coverage run -m unittest \
  tests.test_unit_password_policy \
  tests.test_unit_token_service -v
coverage report -m
```

Sin cobertura (solo ejecución):

```bash
python3 -m unittest \
  tests.test_unit_password_policy \
  tests.test_unit_token_service -v
```

## Generar reportes adicionales

### Reporte XML (CI / SonarQube)

Útil para integración con GitHub Actions, SonarQube u otras herramientas de
análisis estático:

```bash
coverage xml
```

Esto genera el archivo `coverage.xml` en la raíz del proyecto.

### Reporte HTML

Para inspeccionar visualmente qué líneas fueron cubiertas:

```bash
coverage html
```

El reporte se genera en `htmlcov/index.html`.

## Notas para Windows

En Windows el ejecutable `coverage` puede no estar en el `PATH`. Usa `py -m coverage` o `python -m coverage` como prefijo:

```powershell
py -m pip install --upgrade pip coverage
py -m coverage run -m unittest discover -s tests -v
py -m coverage report -m
py -m coverage xml
py -m coverage html
```

Si `py` no está disponible, reemplázalo por `python`.

## Archivos de prueba disponibles

| Archivo | Nivel |
|---------|-------|
| `tests/test_unit_password_policy.py` | Unitario |
| `tests/test_unit_token_service.py` | Unitario |
| `tests/test_integration_password_reset_service.py` | Integración |
| `tests/test_functional_password_reset.py` | Funcional |