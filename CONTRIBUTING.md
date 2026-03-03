# Guía de contribución

Gracias por querer mejorar este ejemplo. La idea de este repositorio es que cualquier estudiante pueda proponer cambios pequeños, justificarlos con evidencia y aprender a trabajar con un flujo simple de GitHub.

## Antes de empezar

1. Revisa el contexto general en [`README.md`](README.md).
2. Si vas a corregir un defecto o agregar cobertura, crea primero un issue o usa uno existente.
3. Mantén los cambios pequeños y fáciles de revisar

## Preparar el entorno

Desde la raíz del repositorio:

```bash
python3 run_example.py
python3 -m unittest discover -s tests -v
```

Si necesitas cobertura:

```bash
python3 -m pip install --upgrade pip coverage
coverage run -m unittest discover -s tests -v
coverage report -m
```

## Flujo de trabajo recomendado

1. Crea una rama a partir de `main`.
2. Usa un nombre descriptivo, por ejemplo `fix/token-expirado` o `test/cobertura-reset`.
3. Implementa el cambio mínimo necesario.
4. Agrega o ajusta pruebas cuando el cambio lo requiera.
5. Ejecuta la suite antes de abrir el Pull Request

## Qué se espera en un Pull Request

- una descripción breve y concreta del cambio
- referencia al issue relacionado, si existe
- evidencia de pruebas ejecutadas
- explicación del riesgo o impacto del cambio

Puedes usar la plantilla en [`.github/pull_request_template.md`](.github/pull_request_template.md).

## Criterios de aceptación

Antes de enviar un cambio, verifica esto:

- el ejemplo sigue ejecutando `run_example.py`
- la suite `unittest` pasa completa
- el cambio no rompe el flujo principal de recuperación
- la documentación refleja el comportamiento nuevo si hubo cambios funcionales
- el PR deja clara la relación entre hallazgo, corrección y evidencia

## Ideas de contribución útiles

- mejorar mensajes mostrados al usuario
- agregar nuevos casos de prueba
- documentar hallazgos en `quality/github-issues/`
- fortalecer validaciones del flujo
- mejorar la trazabilidad entre pruebas, issues y mejoras

## Estilo de contribución

- prioriza claridad sobre complejidad
- evita agregar dependencias sin una necesidad real
- documenta solo lo necesario para que el cambio se entienda
- si el cambio es docente o de demostración, procura que también sea útil para el estudiante que lo lea por primera vez
