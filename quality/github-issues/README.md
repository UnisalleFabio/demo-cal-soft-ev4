# GitHub Issues — Registro de hallazgos

Este directorio contiene la documentación local de los hallazgos (issues)
del proyecto **ejemplo-recuperacion-contraseña**.

## Relación con GitHub Issues

Los archivos `.md` de este directorio son el respaldo local de las issues
creadas en el repositorio de GitHub. Para crear una issue real se usa
GitHub CLI (`gh`):

```bash
gh issue create --repo UnisalleFabio/demo-cal-soft-ev4 \
  --title "INC-01: El correo no informa la expiración del token" \
  --body "Descripción del hallazgo..." \
  --label bug
```

### Requisitos

```bash
winget install GitHub.cli
gh auth login
```

## Por qué se usa el prefijo INC

**INC** significa **Incidencia**. Se usa para identificar defectos o
comportamientos inesperados detectados durante las pruebas. Es una convención
tomada de marcos de gestión de servicios como **ITIL**, donde una incidencia
es un evento no planificado que interrumpe o reduce la calidad de un servicio.

En este proyecto los 3 hallazgos registrados son incidencias:

| ID | Descripción |
|----|-------------|
| INC-01 | El correo no informa la expiración del token |
| INC-02 | No existe limitación de intentos fallidos |
| INC-03 | El usuario no recibe aviso cuando el token ya fue usado |

## Otras siglas comunes

Dependiendo del tipo de hallazgo se pueden usar distintos prefijos:

| Sigla | Significado | Cuándo usarla |
|-------|-------------|---------------|
| **INC** | Incidencia | Defecto o comportamiento inesperado detectado en pruebas |
| **BUG** | Bug | Sinónimo informal de incidencia, común en equipos de desarrollo |
| **HU** | Historia de Usuario | Requisito funcional descrito desde la perspectiva del usuario |
| **RF** | Requisito Funcional | Funcionalidad que el sistema debe cumplir |
| **RNF** | Requisito No Funcional | Restricción de rendimiento, seguridad, usabilidad, etc. |
| **MEJ** | Mejora | Optimización o mejora a funcionalidad existente |
| **TEC** | Tarea Técnica | Trabajo interno (refactoring, deuda técnica, infraestructura) |
| **CHG** | Change Request | Solicitud de cambio formal sobre un requisito ya aprobado |
| **TSK** | Task | Tarea genérica de trabajo dentro de un sprint o iteración |

## Ejemplo de uso combinado en un proyecto

```
HU-01   → Historia de usuario: recuperar contraseña
RF-01   → El sistema debe enviar un enlace de recuperación por correo
RNF-01  → El enlace debe expirar en máximo 30 minutos
INC-01  → El correo no informa la expiración del token
MEJ-01  → Agregar contador de tiempo restante en la interfaz
TEC-01  → Migrar servicio de notificaciones a async
```

## Estructura de un archivo de hallazgo

Cada archivo `.md` sigue esta estructura:

```markdown
# INC-XX - Título descriptivo

- Estado: `Open` | `Closed`
- Tipo: `bug` | `test-gap` | `mejora`
- Severidad: `alta` | `media` | `baja`
- Módulo: nombre del módulo afectado
- Caso asociado: ID del caso de prueba

## Descripción
## Resultado esperado
## Resultado actual
## Impacto
## Evidencia
```