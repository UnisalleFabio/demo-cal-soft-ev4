# Recuperacion de contrasena para un aula virtual

Este repositorio contiene un ejemplo pequeno en Python de un flujo de recuperacion de contrasena para una plataforma academica. Sirve para dos usos concretos:

- practicar un caso sencillo de analisis, pruebas y mejora continua;
- mostrar en GitHub como se integran Issues, Pull Requests y GitHub Actions en un proyecto realista.

El proyecto no depende de una base de datos ni de servicios externos. Todo el flujo se ejecuta en memoria para que puedas revisar el codigo, correr las pruebas y entender el proceso completo sin configuracion adicional.

## Que vas a encontrar aqui

- solicitud de recuperacion por correo;
- generacion y validacion de token;
- restablecimiento de contrasena;
- registro de auditoria del flujo;
- pruebas unitarias, funcionales e integradas;
- artefactos de calidad para seguimiento y mejora;
- automatizacion con GitHub Actions;
- plantillas para registrar incidencias y brechas de prueba en GitHub Issues.

## Requisitos

- Python 3.12 o una version compatible con las caracteristicas usadas en el codigo.

## Ejecucion rapida

Desde la raiz del repositorio:

```bash
python3 run_example.py
```

El script muestra un recorrido completo:

1. el usuario solicita recuperar su contrasena;
2. el sistema genera un token y simula el envio de una notificacion;
3. el usuario restablece la contrasena;
4. el sistema registra los eventos de auditoria.

## Ejecutar las pruebas

```bash
python3 -m unittest discover -s tests -v
```

Si tambien quieres revisar cobertura:

```bash
python3 -m pip install --upgrade pip coverage
coverage run -m unittest discover -s tests -v
coverage report -m
coverage xml
```

## Como usar este repositorio si eres estudiante

Una forma simple de trabajar con el ejemplo es esta:

1. Ejecuta `run_example.py` para entender el flujo.
2. Revisa las pruebas en [`tests/`](tests/) para ver que valida cada nivel.
3. Explora los documentos de [`quality/`](quality/) para relacionar pruebas, hallazgos y mejoras.
4. Crea un issue usando una plantilla de [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/).
5. Propone un cambio en una rama y abre un Pull Request.
6. Revisa el resultado de GitHub Actions como evidencia tecnica del cambio.

## Integracion con GitHub

### GitHub Issues

El repositorio ya incluye plantillas listas para usar:

- [`.github/ISSUE_TEMPLATE/bug_report.yml`](.github/ISSUE_TEMPLATE/bug_report.yml) para defectos;
- [`.github/ISSUE_TEMPLATE/test_gap.yml`](.github/ISSUE_TEMPLATE/test_gap.yml) para brechas de cobertura.

Ademas, en [`quality/github-issues/`](quality/github-issues/) tienes ejemplos de incidencias que puedes llevar a GitHub para una demostracion o para practicar trazabilidad.

### Pull Requests

El archivo [`.github/pull_request_template.md`](.github/pull_request_template.md) deja una estructura minima para documentar:

- resumen del cambio;
- evidencia de pruebas;
- issue relacionado;
- riesgos o puntos de revision.

### GitHub Actions

El workflow [`.github/workflows/ci.yml`](.github/workflows/ci.yml) queda listo para ejecutarse en GitHub cuando publiques este directorio como repositorio independiente. La automatizacion:

- instala `coverage`;
- ejecuta la suite completa;
- imprime el reporte de cobertura;
- genera `coverage.xml`;
- publica `coverage.xml` como artefacto del workflow.

## Flujo sugerido en GitHub

Si publicas este proyecto en GitHub, una dinamica simple para la clase o para trabajo individual es esta:

1. registrar un defecto o una brecha con GitHub Issues;
2. crear una rama corta para resolver el hallazgo;
3. implementar el cambio y ejecutar pruebas;
4. abrir un Pull Request con evidencia;
5. revisar el resultado del workflow de GitHub Actions;
6. cerrar el issue cuando el cambio quede integrado.

## Estructura del proyecto

- [`src/virtual_campus/`](src/virtual_campus/): codigo fuente del modulo.
- [`tests/`](tests/): pruebas unitarias, funcionales e integradas.
- [`quality/`](quality/): evidencias, seguimiento, checklist y mejora continua.
- [`.github/`](.github/): integracion con GitHub Issues, Pull Requests y Actions.
- [`run_example.py`](run_example.py): ejecucion guiada del flujo principal.

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

Este proyecto esta pensado para aprendizaje y demostracion. No implementa:

- persistencia real en base de datos;
- envio real de correos;
- interfaz web;
- autenticacion integrada con otros servicios.

Su objetivo es que puedas concentrarte en el flujo, las pruebas y la evidencia de calidad.

## Contribuciones y licencia

Las pautas de colaboracion estan en [`CONTRIBUTING.md`](CONTRIBUTING.md). El repositorio se distribuye bajo la licencia [`MIT`](LICENSE).
