# Modelo de datos inicial

## Propósito

El modelo conserva las métricas publicadas para cada título y semestre, permitiendo comparar periodos sin alterar el archivo original. Se implementará en PostgreSQL y se reutilizará como base del modelo estrella en Power BI.

## Grano de la tabla de hechos

Una fila en `fact_title_period` representa **un título, un tipo de contenido y un periodo de reporte**. No se agregan filas antes de cargar los datos.

## Esquema propuesto

```text
dim_period (1) ────< fact_title_period >──── (1) dim_title
                              │
                              ├────────────── (1) dim_content_type
                              └────────────── (0..1) dim_availability
```

| Tabla | Propósito | Campos iniciales |
|---|---|---|
| `dim_period` | Define cada semestre analizado. | `period_key`, `period_label`, `start_date`, `end_date`, `report_published_date` |
| `dim_title` | Describe el título tal como aparece en la fuente. | `title_key`, `title_display_name`, `title_normalized_name`, `release_date`, `runtime_hours`, `source_title_id` |
| `dim_content_type` | Estandariza película/serie u otros valores publicados. | `content_type_key`, `content_type_name`, `source_content_type` |
| `dim_availability` | Conserva la clasificación de disponibilidad publicada. | `availability_key`, `availability_label`, `is_globally_available` |
| `fact_title_period` | Métricas por título y periodo. | `period_key`, `title_key`, `content_type_key`, `availability_key`, `hours_viewed`, `views`, `global_rank`, `source_file_name`, `loaded_at` |

## Reglas de identidad

- Se preservará un identificador de título de origen cuando el archivo lo incluya.
- Si no existe, la clave técnica se generará a partir del nombre normalizado y el tipo de contenido, sin asumir que constituye una identidad editorial perfecta.
- Un título con coincidencia ambigua entre periodos se marcará para revisión; no se consolidará manualmente sin una regla documentada.
- Temporadas, series y franquicias solo se analizarán si pueden identificarse de forma confiable con campos de origen o una tabla de mapeo auditable.

## Métricas derivadas previstas

- Participación de horas vistas y visualizaciones por periodo.
- Ranking y percentil de rendimiento dentro del periodo.
- Variación de métricas respecto del semestre anterior mediante `LAG`.
- Indicador de persistencia para títulos presentes en periodos consecutivos.
- Acumulado Pareto y participación acumulada por título.

## Controles de calidad mínimos

1. Unicidad de la combinación de título, tipo y periodo.
2. Horas vistas, visualizaciones y duración no negativas.
3. Valores de tipo y disponibilidad dentro de catálogos estandarizados.
4. Conteo de registros cargados igual al esperado para cada fuente, salvo exclusiones registradas.
5. No calcular comparaciones entre periodos cuya definición de métricas no sea compatible.
