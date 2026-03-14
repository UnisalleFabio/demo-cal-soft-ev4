# Recuperación de contraseña para un aula virtual

Este repositorio contiene un ejemplo pequeño en Python de un flujo de recuperación de contraseña para una plataforma académica. Sirve para dos usos concretos:

- practicar un caso sencillo de análisis, pruebas y mejora continua
- mostrar en GitHub cómo se integran Issues, Pull Requests y GitHub Actions en un proyecto realista

El proyecto no depende de una base de datos ni de servicios externos. Todo el flujo se ejecuta en memoria para que puedas revisar el código, correr las pruebas y entender el proceso completo sin configuración adicional.

## Qué vas a encontrar aquí

- solicitud de recuperación por correo
- generación y validación de token
- restablecimiento de contraseña
- registro de auditoría del flujo
- pruebas unitarias, funcionales e integradas
- ejemplos de pruebas no funcionales de carga, usabilidad y seguridad
- artefactos de calidad para seguimiento y mejora
- automatización con GitHub Actions
- plantillas para registrar incidencias y brechas de prueba en GitHub Issues

## Requisitos

- Python 3.12 o una versión compatible con las características usadas en el código

## Ejecución rápida

Desde la raíz del repositorio:

```bash
python3 run_example.py
```

El script muestra un recorrido completo:

1. El usuario solicita recuperar su contraseña
2. El sistema genera un token y simula el envío de una notificación
3. El usuario restablece la contraseña
4. El sistema registra los eventos de auditoría

## Ejecutar las pruebas

```bash
python3 -m unittest discover -s tests -v
```

El repositorio también incluye ejemplos no funcionales en
`tests/test_non_functional_examples.py`. Si quieres correr solo esos casos:

```bash
python3 -m unittest discover -s tests -p 'test_non_functional_examples.py' -v
```

Si también quieres revisar cobertura:

```bash
python3 -m pip install --upgrade pip coverage
coverage run -m unittest discover -s tests -v
coverage report -m
coverage xml
```

## Ejemplos de pruebas no funcionales

La suite agrega un archivo con ejemplos sencillos y ejecutables para clase:

- carga ligera sobre `200` flujos completos en memoria
- usabilidad centrada en claridad de mensajes y pasos del proceso
- seguridad centrada en expiración, no reutilización y auditoría del token

La explicación de alcance y límites está en
[`quality/non-functional/README.md`](quality/non-functional/README.md).

## Cómo usar este repositorio si eres estudiante

Una forma simple de trabajar con el ejemplo es esta:

1. Ejecuta `run_example.py` para entender el flujo.
2. Revisa las pruebas en [`tests/`](tests/) para ver que valida cada nivel.
3. Explora los documentos de [`quality/`](quality/) para relacionar pruebas, hallazgos y mejoras.
4. Crea un issue usando una plantilla de [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/).
5. Propone un cambio en una rama y abre un Pull Request.
6. Revisa el resultado de GitHub Actions como evidencia técnica del cambio

## Integración con GitHub

### GitHub Issues

El repositorio ya incluye plantillas listas para usar:

- [`.github/ISSUE_TEMPLATE/bug_report.yml`](.github/ISSUE_TEMPLATE/bug_report.yml) para defectos
- [`.github/ISSUE_TEMPLATE/test_gap.yml`](.github/ISSUE_TEMPLATE/test_gap.yml) para brechas de cobertura

Además, en [`quality/github-issues/`](quality/github-issues/) tienes ejemplos de incidencias que puedes llevar a GitHub para una demostración o para practicar trazabilidad.

### Pull Requests

El archivo [`.github/pull_request_template.md`](.github/pull_request_template.md) deja una estructura mínima para documentar:

- resumen del cambio
- evidencia de pruebas
- issue relacionado
- riesgos o puntos de revisión

### GitHub Actions

El workflow [`.github/workflows/ci.yml`](.github/workflows/ci.yml) queda listo para ejecutarse en GitHub cuando publiques este directorio como repositorio independiente. La automatización:

- instala `coverage`
- ejecuta la suite completa
- imprime el reporte de cobertura
- genera `coverage.xml`
- publica `coverage.xml` como artefacto del workflow

## Flujo sugerido en GitHub

Si publicas este proyecto en GitHub, una dinámica simple para la clase o para trabajo individual es esta:

1. Registrar un defecto o una brecha con GitHub Issues
2. Crear una rama corta para resolver el hallazgo
3. Implementar el cambio y ejecutar pruebas
4. Abrir un Pull Request con evidencia
5. Revisar el resultado del workflow de GitHub Actions
6. Cerrar el issue cuando el cambio quede integrado

## Estructura del proyecto

- [`src/virtual_campus/`](src/virtual_campus/): código fuente del módulo
- [`tests/`](tests/): pruebas unitarias, funcionales e integradas
- [`quality/`](quality/): evidencias, seguimiento, checklist y mejora continua
- [`.github/`](.github/): integración con GitHub Issues, Pull Requests y Actions
- [`run_example.py`](run_example.py): ejecución guiada del flujo principal

## Material de apoyo

Si quieres profundizar en el trabajo de calidad del ejemplo, revisa estos archivos:

- [`quality/metricas-y-seguimiento.md`](quality/metricas-y-seguimiento.md)
- [`quality/checklist-revision-codigo.md`](quality/checklist-revision-codigo.md)
- [`quality/plan-mejora-continua.md`](quality/plan-mejora-continua.md)
- [`quality/test-management/README.md`](quality/test-management/README.md)
- [`quality/github-issues/README.md`](quality/github-issues/README.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`LICENSE`](LICENSE)

## Alcance del ejemplo

Este proyecto está pensado para aprendizaje y demostración. No implementa:

- persistencia real en base de datos
- envío real de correos
- interfaz web
- autenticación integrada con otros servicios

Su objetivo es que puedas concentrarte en el flujo, las pruebas y la evidencia de calidad.

## Contribuciones y licencia

Las pautas de colaboración están en [`CONTRIBUTING.md`](CONTRIBUTING.md). El repositorio se distribuye bajo la licencia [`MIT`](LICENSE).
