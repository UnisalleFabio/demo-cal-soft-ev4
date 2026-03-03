# Densidad de Defectos

Métrica que relaciona la cantidad de defectos encontrados con el tamaño del
código fuente, expresada en **defectos por cada mil líneas de código (KLOC)**.

## Fórmula

```
Densidad de defectos = defectos encontrados / KLOC
```

Donde **KLOC** = líneas de código fuente / 1000.

## Cálculo actual del proyecto

### Tamaño del código fuente (`src/`)

| Archivo | Líneas |
|---------|-------:|
| `virtual_campus/__init__.py` | 1 |
| `virtual_campus/app.py` | 41 |
| `virtual_campus/audit.py` | 15 |
| `virtual_campus/entities.py` | 42 |
| `virtual_campus/notifier.py` | 18 |
| `virtual_campus/password_policy.py` | 29 |
| `virtual_campus/repositories.py` | 35 |
| `virtual_campus/reset_service.py` | 71 |
| `virtual_campus/security.py` | 5 |
| `virtual_campus/token_service.py` | 34 |
| **Total** | **291** |

**KLOC** = 291 / 1000 = **0.291**

### Defectos registrados

Tomados de [`quality/github-issues/`](github-issues/):

| ID | Descripción |
|----|-------------|
| INC-01 | Fecha de expiración |
| INC-02 | Intentos fallidos |
| INC-03 | Token usado |

**Total de defectos:** 3

### Resultado

```
Densidad = 3 / 0.291 = 10.31 defectos por KLOC
```

## Interpretación

| Rango (defectos/KLOC) | Interpretación |
|----------------------:|----------------|
| 0 – 5 | Calidad alta |
| 5 – 15 | Calidad aceptable |
| 15 – 30 | Necesita mejora |
| > 30 | Calidad baja |

El proyecto se encuentra en **calidad aceptable** con 10.31 defectos/KLOC.

## Cómo medir las líneas de código

### Opción rápida (incluye líneas en blanco y comentarios)

```bash
wc -l src/virtual_campus/*.py
```

### Opción precisa (solo líneas lógicas)

```bash
pip install pygount
pygount src/ --format=summary
```

`pygount` excluye líneas en blanco y comentarios, dando un conteo más preciso
del código ejecutable.

## Cómo actualizar esta métrica

1. Contar las líneas de código actuales con `wc -l` o `pygount`
2. Contar los defectos registrados en `quality/github-issues/`
3. Aplicar la fórmula y actualizar la tabla de este documento