# Matriz de Trazabilidad

Relación entre requisitos, casos de prueba, ejecuciones y defectos del proyecto
**ejemplo-recuperacion-contraseña**.

## Matriz completa

| Requisito / Funcionalidad | Caso | Tipo | Prioridad | Automatizada | Ejecución | Estado | Hallazgo |
|---------------------------|------|------|-----------|:------------:|-----------|--------|----------|
| Validación de contraseña | U-01 | Unitaria | Alta | si | RUN-01 | passed | INC-02 |
| Expiración de token | U-02 | Unitaria | Media | si | RUN-01 | passed | INC-03 |
| Solicitud de recuperación | F-01 | Funcional | Alta | si | RUN-01 | passed | INC-01 |
| Contenido del mensaje | F-02 | Funcional | Media | no | RUN-01 | failed | INC-01 |
| Reutilización de token | F-03 | Funcional | Media | no | RUN-01 | failed | INC-03 |
| Restablecimiento completo | I-01 | Integrada | Alta | si | RUN-01 | passed | — |
| Intentos fallidos | I-02 | Integrada | Alta | no | RUN-01 | failed | INC-02 |

## Trazabilidad de defectos

Cada defecto vinculado a sus casos de prueba, módulo y evidencia.

| Defecto | Severidad | Módulo | Casos asociados | Evidencia |
|---------|-----------|--------|-----------------|-----------|
| INC-01 | Media | `notifier` | F-01, F-02 | `tests/test_functional_password_reset.py` |
| INC-02 | Alta | `reset_service` | U-01, I-02 | `tests/test_integration_password_reset_service.py` |
| INC-03 | Baja | `token_service` | U-02, F-03 | `tests/test_functional_password_reset.py` |

## Métricas de trazabilidad

### Cobertura de requisitos

```
Casos con prueba definida / total de casos = 7 / 7 = 100%
```

Todos los requisitos identificados tienen al menos un caso de prueba asociado.

### Automatización de pruebas

```
Casos automatizados / total de casos = 4 / 7 = 57.1%
```

| Estado | Casos | Porcentaje |
|--------|:-----:|-----------:|
| Automatizada | 4 | 57.1% |
| Manual | 3 | 42.9% |

Casos pendientes de automatizar: **F-02**, **F-03**, **I-02**.

### Trazabilidad de defectos

```
Defectos con caso asociado / total de defectos = 3 / 3 = 100%
```

Todos los defectos están vinculados a al menos un caso de prueba.

### Tasa de éxito por ejecución (RUN-01)

```
Casos pasados / total ejecutados = 4 / 7 = 57.1%
```

| Estado | Cantidad | Porcentaje |
|--------|:--------:|-----------:|
| passed | 4 | 57.1% |
| failed | 3 | 42.9% |

## Resumen

| Métrica | Valor |
|---------|------:|
| Total de requisitos cubiertos | 100% |
| Automatización de pruebas | 57.1% |
| Defectos trazados | 100% |
| Tasa de éxito (RUN-01) | 57.1% |
| Defectos abiertos | 3 |

## Cómo actualizar esta matriz

1. Al crear un nuevo caso de prueba, agregarlo a
   [`casos-prueba-formales.csv`](test-management/casos-prueba-formales.csv)
   y a la matriz de este documento
2. Al ejecutar una nueva corrida, registrarla en
   [`ejecuciones-prueba.csv`](test-management/ejecuciones-prueba.csv)
   y actualizar el estado en la matriz
3. Al registrar un nuevo defecto en
   [`github-issues/`](github-issues/),
   vincular los casos asociados y actualizar las métricas