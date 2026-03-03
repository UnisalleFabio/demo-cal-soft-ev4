# Severidad de Defectos

Clasificación y análisis de la severidad de los defectos registrados en el
proyecto **ejemplo-recuperacion-contraseña**.

## Escala de severidad

| Nivel | Peso | Criterio |
|-------|-----:|----------|
| **Alta** | 3 | Afecta seguridad, pérdida de datos o bloquea funcionalidad crítica |
| **Media** | 2 | Degrada la experiencia de usuario o reduce claridad del flujo |
| **Baja** | 1 | Problema cosmético, de usabilidad menor o brecha informativa |

## Defectos registrados

| ID | Defecto | Módulo | Severidad |
|----|---------|--------|-----------|
| INC-01 | Correo no informa expiración del token | `notifier` | Media |
| INC-02 | Sin limitación de intentos fallidos | `reset_service` | Alta |
| INC-03 | Sin aviso cuando el token ya fue usado | `token_service` | Baja |

## Distribución por severidad

| Severidad | Cantidad | Porcentaje |
|-----------|:--------:|-----------:|
| Alta | 1 | 33.3% |
| Media | 1 | 33.3% |
| Baja | 1 | 33.3% |
| **Total** | **3** | **100%** |

## Índice de severidad ponderado

Permite resumir en un solo número qué tan graves son los defectos en promedio.

```
Índice = (alta × 3 + media × 2 + baja × 1) / total de defectos
```

### Cálculo actual

```
Índice = (1 × 3 + 1 × 2 + 1 × 1) / 3
       = (3 + 2 + 1) / 3
       = 6 / 3
       = 2.0
```

### Interpretación

| Rango | Interpretación |
|------:|----------------|
| 1.0 – 1.5 | Defectos mayormente leves |
| 1.5 – 2.0 | Severidad promedio media |
| 2.0 – 2.5 | Tendencia hacia defectos graves |
| 2.5 – 3.0 | Defectos mayormente críticos |

El proyecto presenta un índice de **2.0**, lo que indica una severidad
promedio **media**.

## Prioridad de resolución sugerida

Basada en severidad e impacto:

| Prioridad | ID | Razón |
|:---------:|----|-------|
| 1 | INC-02 | Riesgo de seguridad: permite abuso del flujo sin restricción |
| 2 | INC-01 | Afecta experiencia de usuario y genera carga en soporte |
| 3 | INC-03 | Problema de usabilidad menor, el sistema sí rechaza el token |

## Cómo actualizar esta métrica

1. Asignar severidad (alta, media o baja) a cada nuevo defecto en
   [`quality/github-issues/`](github-issues/)
2. Actualizar las tablas de distribución y el cálculo del índice ponderado
3. Revisar la prioridad de resolución según el nuevo panorama
