# GitHub Actions — Integración Continua

Documentación del pipeline de integración continua (CI) del proyecto
**ejemplo-recuperacion-contraseña**.

## Qué hace ahora el workflow

El archivo de configuración está en
[`.github/workflows/ci.yml`](../../.github/workflows/ci.yml).

El flujo se ejecuta en cada `push` y en cada `pull_request`, y quedó dividido
en jobs separados para que la evidencia sea más clara en clase.

## Jobs del pipeline

| Job | Propósito | Resultado principal |
|---|---|---|
| `build` | Genera un ejecutable para Ubuntu con `PyInstaller`. | Artefacto `ubuntu-executable` |
| `unit_tests` | Ejecuta las pruebas unitarias. | Artefacto `unit-test-results` |
| `integration_tests` | Ejecuta las pruebas de integración. | Artefacto `integration-test-results` |
| `functional_tests` | Ejecuta las pruebas funcionales. | Artefacto `functional-test-results` |
| `non_functional_tests` | Ejecuta las pruebas no funcionales. | Artefacto `non-functional-test-results` |
| `coverage` | Ejecuta la suite completa con cobertura. | Artefacto `coverage-xml` |
| `pipeline_ok` | Publica una notificación final cuando todo terminó bien. | Resumen final en `Actions` |

## Orden del flujo

```text
push / pull_request
        |
        v
      build
        |
        +--> unit_tests
        +--> integration_tests
        +--> functional_tests
        +--> non_functional_tests
                    |
                    v
                 coverage
                    |
                    v
                pipeline_ok
```

Si el job `build` falla, los jobs de pruebas no continúan porque todos dependen
de `build`.

## Artefactos que publica GitHub Actions

### Build

- `ubuntu-executable`: incluye el binario `dist/ejemplo-recuperacion-contrasena`
  y un empaquetado `dist/ejemplo-recuperacion-contrasena-linux.tar.gz`.

### Pruebas

Cada suite publica un archivo JSON con el resumen de la ejecución:

- `unit-test-results`
- `integration-test-results`
- `functional-test-results`
- `non-functional-test-results`

Cada JSON deja evidencia de:

- cuántas pruebas se ejecutaron;
- cuántas aprobaron;
- cuántos fallos y errores hubo;
- si la suite fue exitosa o no.

### Cobertura

- `coverage-xml`: contiene `coverage.xml`, útil para herramientas externas como
  SonarQube, Codecov o Coveralls.

## Cómo se notifican los estados

El workflow usa dos mecanismos simples de notificación dentro de GitHub Actions:

- mensajes `::notice::` cuando una etapa termina correctamente;
- mensajes `::error::` cuando una etapa falla;
- resúmenes escritos en `GITHUB_STEP_SUMMARY` para que cada job deje evidencia
  fácil de leer.

Además, el job `pipeline_ok` deja una notificación final cuando el build, las
cuatro suites y la cobertura terminan sin errores.

## Dónde ver logs y resultados

1. Abrir el repositorio en GitHub.
2. Entrar en la pestaña **Actions**.
3. Seleccionar una ejecución del workflow.
4. Abrir el job que quieres revisar.
5. Entrar a cada step para ver el log detallado.

En la misma ejecución puedes revisar:

- la sección **Artifacts** para descargar binarios y resúmenes;
- la pestaña o bloque de **Summary** para leer las notificaciones de cada job.

## Cómo ejecutar algo parecido localmente en Ubuntu

### Build del ejecutable

```bash
python3 -m pip install --upgrade pip pyinstaller
pyinstaller --onefile --name ejemplo-recuperacion-contrasena run_example.py
```

El binario quedará en:

```text
dist/ejemplo-recuperacion-contrasena
```

### Ejecución por suite

```bash
python3 scripts/run_unittest_suite.py \
  --suite-name "pruebas unitarias" \
  --pattern "test_unit*.py" \
  --results-file "artifacts/unit-test-results.json"
```

Puedes cambiar el patrón para las demás suites:

- `test_integration*.py`
- `test_functional*.py`
- `test_non_functional*.py`

### Cobertura

```bash
python3 -m pip install --upgrade pip coverage
coverage run -m unittest discover -s tests -v
coverage report -m
coverage xml
```

## Script auxiliar usado por el CI

El archivo [`scripts/run_unittest_suite.py`](../../scripts/run_unittest_suite.py)
ejecuta una suite `unittest`, guarda un resumen en JSON y expone totales a
GitHub Actions para que el workflow pueda:

- notificar cuántas pruebas pasaron;
- subir un artefacto por suite;
- fallar el job si la suite falla o si no se descubre ninguna prueba.
