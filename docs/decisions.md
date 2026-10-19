# Decisiones, supuestos, pendientes y limitaciones

## Decisiones confirmadas

| ID | Decisión | Motivo |
|---|---|---|
| D-01 | Usar reportes públicos oficiales *What We Watched* de Netflix como fuente principal. | Mantener trazabilidad y evitar datos inventados. |
| D-02 | Usar el semestre como periodo analítico principal. | Es la periodicidad de publicación prevista. |
| D-03 | Priorizar un pipeline reproducible y hallazgos defendibles sobre funciones adicionales. | Adecuado al objetivo de portafolio de una semana. |
| D-04 | Mantener datos crudos sin modificar y generar los procesados mediante scripts. | Permite auditoría y repetición del análisis. |
| D-05 | No presentar el proyecto como afiliado a Netflix. | Refleja correctamente la procedencia pública de los datos. |

## Supuestos por validar con las fuentes

| ID | Supuesto | Acción de validación |
|---|---|---|
| S-01 | Los archivos de 2023 en adelante contienen campos comparables de título, periodo y métricas. | Revisar esquemas durante la ingestión. |
| S-02 | La disponibilidad global, fecha de estreno y duración aparecen en todos o algunos reportes. | Registrar cobertura por periodo y no imputar faltantes. |
| S-03 | El nombre y tipo de contenido permiten vincular algunos títulos entre semestres. | Medir coincidencias y revisar ambigüedades. |

## Pendientes

| ID | Pendiente | Estado |
|---|---|---|
| P-01 | Seleccionar y registrar los archivos oficiales concretos desde 2023. | Pendiente |
| P-02 | Confirmar el esquema real de cada archivo y sus cambios. | Pendiente |
| P-03 | Definir el alcance final de páginas de Excel y Power BI tras el perfilado. | Pendiente |
| P-04 | Decidir si se incorporará enriquecimiento externo verificable. | Fuera del MVP por ahora |

## Limitaciones previstas

- Los datos son agregados por título y periodo; no representan usuarios individuales ni retención real de audiencia.
- Las inferencias de catálogo, estrenos, temporadas o franquicias dependerán de los campos disponibles y sus reglas explícitas.
- La comparación entre periodos estará condicionada a que Netflix conserve definiciones compatibles de las métricas.
