# GitHub Actions — Integración Continua

Documentación del pipeline de integración continua (CI) del proyecto
**ejemplo-recuperacion-contraseña**.

## Qué es GitHub Actions

GitHub Actions es el servicio de CI/CD integrado en GitHub. Permite ejecutar
flujos de trabajo automatizados (workflows) en respuesta a eventos del
repositorio como `push`, `pull_request`, creación de tags, etc.

En este proyecto se usa para:

- Ejecutar automáticamente todas las pruebas en cada cambio
- Medir la cobertura de código
- Generar y almacenar el reporte de cobertura como artefacto

## Workflow actual

El archivo de configuración se encuentra en
[`.github/workflows/ci.yml`](../../.github/workflows/ci.yml).

### Cuándo se ejecuta

```yaml
on:
  push:
  pull_request:
```

Se activa en **cada push** a cualquier rama y en **cada pull request**.

### Qué hace paso a paso

| Paso | Acción | Descripción |
|:----:|--------|-------------|
| 1 | `actions/checkout@v4` | Descarga el código del repositorio |
| 2 | `actions/setup-python@v5` | Configura Python 3.12 en el runner |
| 3 | `pip install coverage` | Instala la herramienta de cobertura |
| 4 | `coverage run -m unittest discover` | Ejecuta todas las pruebas (unitarias, integración y funcionales) midiendo cobertura |
| 5 | `coverage report -m` | Muestra el reporte de cobertura en consola |
| 6 | `coverage xml` | Genera `coverage.xml` para herramientas externas |
| 7 | `actions/upload-artifact@v4` | Sube `coverage.xml` como artefacto descargable |

### Diagrama del flujo

```
push / pull_request
       │
       ▼
  ┌──────────┐
  │ Checkout  │
  └────┬─────┘
       ▼
  ┌──────────────┐
  │ Setup Python │
  │    3.12      │
  └────┬─────────┘
       ▼
  ┌──────────────────┐
  │ Install coverage │
  └────┬─────────────┘
       ▼
  ┌───────────────────────────┐
  │ Run tests con cobertura   │
  │ unittest discover -s tests│
  └────┬──────────────────────┘
       ▼
  ┌──────────────────┐
  │ Coverage report  │
  └────┬─────────────┘
       ▼
  ┌──────────────────┐
  │ Coverage XML     │
  └────┬─────────────┘
       ▼
  ┌──────────────────────┐
  │ Upload artifact      │
  │ (coverage.xml)       │
  └──────────────────────┘
```

## Cómo ver los resultados

1. Ir al repositorio en GitHub: `https://github.com/UnisalleFabio/demo-cal-soft-ev4`
2. Hacer clic en la pestaña **Actions**
3. Seleccionar la ejecución (run) que se quiere revisar
4. Hacer clic en el job **test** para ver el log de cada paso

### Indicadores de estado

| Icono | Significado |
|:-----:|-------------|
| ✅ | Todas las pruebas pasaron |
| ❌ | Al menos una prueba falló o hubo un error |
| 🟡 | La ejecución está en progreso |

## Cómo descargar el artefacto de cobertura

1. En la pestaña **Actions**, seleccionar una ejecución completada
2. En la sección **Artifacts** (parte inferior), hacer clic en **coverage-xml**
3. Se descarga un `.zip` que contiene `coverage.xml`

Este archivo se puede usar con herramientas como:

- **SonarQube** para análisis de calidad
- **Codecov** o **Coveralls** para reportes visuales de cobertura
- Cualquier herramienta que soporte el formato Cobertura XML

## Cómo ejecutar el CI localmente

Para replicar lo que hace el CI en tu máquina local:

```bash
# Con Python 3.12+ (Linux/Mac)
python3 -m pip install --upgrade pip coverage
coverage run -m unittest discover -s tests -v
coverage report -m
coverage xml
```

```powershell
# Con Python 3.13 (Windows)
py -3.13 -m pip install --upgrade pip coverage
py -3.13 -m coverage run -m unittest discover -s tests -v
py -3.13 -m coverage report -m
py -3.13 -m coverage xml
```

## Estructura del archivo ci.yml

```yaml
name: ejemplo-recuperacion-contrasena-ci    # Nombre del workflow

on:
  push:                                      # Se ejecuta en cada push
  pull_request:                              # Se ejecuta en cada PR

jobs:
  test:                                      # Nombre del job
    runs-on: ubuntu-latest                   # Sistema operativo del runner
    steps:
      - name: Checkout
        uses: actions/checkout@v4            # Clona el repositorio

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"             # Versión de Python

      - name: Install tooling
        run: python -m pip install --upgrade pip coverage

      - name: Run unit, functional and integration tests
        run: coverage run -m unittest discover -s tests -v

      - name: Show coverage report
        run: coverage report -m

      - name: Export coverage xml
        run: coverage xml

      - name: Upload coverage artifact
        uses: actions/upload-artifact@v4
        with:
          name: coverage-xml
          path: coverage.xml                 # Archivo que se sube
```
