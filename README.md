# StreamScope Analytics

Proyecto de portafolio de análisis de audiencia y rendimiento de contenido de streaming, construido con reportes públicos oficiales *What We Watched* de Netflix. Integra Python/pandas, PostgreSQL, SQL, Excel con Power Query y Power BI para analizar desempeño de títulos, concentración del consumo y persistencia entre periodos.

> Este proyecto es independiente y no está afiliado, patrocinado ni aprobado por Netflix.

## Estado del proyecto

Fase actual: diseño confirmado. La ingestión empezará después de registrar y descargar las fuentes oficiales seleccionadas.

## Preguntas analíticas

1. ¿Qué proporción del consumo corresponde a estrenos frente a catálogo?
2. ¿Qué títulos persisten entre semestres y cómo cambia su rendimiento?
3. ¿Qué tan concentrado está el consumo?
4. ¿Cómo evolucionan horas vistas y visualizaciones?
5. ¿Qué relación existe entre duración, horas vistas y visualizaciones?
6. Cuando la fuente lo permita, ¿la disponibilidad global se asocia con mayor alcance?

## Estructura

```text
data/raw/          # fuentes descargadas, sin modificación
data/processed/    # conjuntos limpios generados por el pipeline
docs/              # fuentes, modelo, decisiones y documentación
src/               # scripts de ingestión, limpieza y validación
sql/ddl/           # definición de esquema PostgreSQL
sql/views/         # vistas analíticas
sql/queries/       # consultas y controles de calidad
tests/             # pruebas automatizadas o de validación
excel/             # libro Excel 365
powerbi/           # archivo Power BI y documentación asociada
notebooks/         # exploración, no fuente de verdad del pipeline
```

Los datos de `data/raw/` y `data/processed/` no se versionarán si su tamaño o condiciones de distribución lo desaconsejan; el pipeline y el inventario de fuentes sí deben permitir reproducirlos.

## Documentación de diseño

- [Modelo de datos](docs/data_model.md)
- [Decisiones, supuestos y limitaciones](docs/decisions.md)
- [Inventario de fuentes](docs/sources.md)

## Reproducibilidad

Las instrucciones de ejecución se completarán al implementar la ingestión. Ningún resultado analítico se publicará sin poder rastrearlo a una fuente y transformación documentadas.
