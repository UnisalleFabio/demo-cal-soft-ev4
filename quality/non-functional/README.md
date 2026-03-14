# Pruebas no funcionales de ejemplo

Este directorio documenta los ejemplos didácticos de pruebas no funcionales
agregados al repositorio. Los casos automatizados viven en
`tests/test_non_functional_examples.py`.

## Qué cubre cada ejemplo

### Carga

- Simula `200` flujos completos de recuperación en memoria.
- Usa un umbral didáctico de `2.5` segundos para mostrar una verificación
  básica de rendimiento.
- Sirve para conversar sobre la diferencia entre una prueba de humo bajo carga
  y una prueba de estrés real.

### Usabilidad

- Verifica que el mensaje inicial sea consistente para correos válidos y no
  válidos.
- Revisa que la notificación diga claramente cuál es el siguiente paso.
- Confirma que la retroalimentación de la política de contraseñas sea
  accionable para el usuario.

### Seguridad

- Comprueba que los tokens expiren.
- Comprueba que un token usado no pueda reutilizarse.
- Verifica que el token no termine guardado en el log de auditoría.

## Cómo ejecutarlos

Desde la raiz del proyecto:

```bash
python3 -m unittest discover -s tests -p 'test_non_functional_examples.py' -v
```

También quedan incluidos en la suite completa:

```bash
python3 -m unittest discover -s tests -v
```

## Límites del ejemplo

- No reemplaza herramientas especializadas como `Locust`, `k6` o `OWASP ZAP`.
- No hay interfaz gráfica real, así que la usabilidad se evalúa a través de la
  claridad del flujo y de los mensajes.
- La carga es intencionalmente ligera para que el ejemplo siga siendo estable
  en clase y en `CI`.
