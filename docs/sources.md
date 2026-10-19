# Inventario de fuentes

El alcance inicial cubre cinco semestres consecutivos, de enero de 2023 a junio de 2025. Cada fuente es un archivo Excel publicado por Netflix en su sitio institucional. La descarga, la huella SHA-256 y el conteo de filas quedaron registrados en [source_manifest.csv](source_manifest.csv).

| source_id | Periodo cubierto | Página oficial | Archivo Excel oficial | Fecha de consulta | Estado |
|---|---|---|---|---|---|
| NFLX_WWW_2023_H1 | Ene–jun 2023 | [Anuncio del informe](https://about.netflix.com/en/news/what-we-watched-a-netflix-engagement-report) | [XLSX](https://assets.ctfassets.net/4cd45et68cgf/1HyknFM84ISQpeua6TjM7A/97a0a393098937a8f29c9d29c48dbfa8/What_We_Watched_A_Netflix_Engagement_Report_2023Jan-Jun.xlsx) | 2026-10-19 | Descargada y verificada |
| NFLX_WWW_2023_H2 | Jul–dic 2023 | [Anuncio del informe](https://about.netflix.com/en/news/what-we-watched-the-second-half-of-2023) | [XLSX](https://assets.ctfassets.net/4cd45et68cgf/inuAnzotdsAEgbInGLzH5/1be323ba419b2af3a96bffa29acc31a3/What_We_Watched_A_Netflix_Engagement_Report_2023Jul-Dec.xlsx) | 2026-10-19 | Descargada y verificada |
| NFLX_WWW_2024_H1 | Ene–jun 2024 | [Anuncio del informe](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2024) | [XLSX](https://assets.ctfassets.net/4cd45et68cgf/2PoZlfdc46dH2gQvI8eUzI/9db5840720c47acfcf7b89ffe2402860/What_We_Watched_A_Netflix_Engagement_Report_2024Jan-Jun.xlsx) | 2026-10-19 | Descargada y verificada |
| NFLX_WWW_2024_H2 | Jul–dic 2024 | [Anuncio del informe](https://about.netflix.com/en/news/what-we-watched-the-second-half-of-2024) | [XLSX](https://assets.ctfassets.net/4cd45et68cgf/6XSmoEjBjVMPRtYybT9d1E/8c0b0b2645b8712d5597b0bdbe0d64e2/What_We_Watched_A_Netflix_Engagement_Report_2024Jul-Dec.xlsx) | 2026-10-19 | Descargada y verificada |
| NFLX_WWW_2025_H1 | Ene–jun 2025 | [Anuncio del informe](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2025) | [XLSX](https://assets.ctfassets.net/4cd45et68cgf/mplcXj5ulHDfbCPCr0f0I/5dbb6ec09f03df89706476e380e9b8bd/What_We_Watched_A_Netflix_Engagement_Report_2025Jan-Jun.xlsx) | 2026-10-19 | Descargada y verificada |

## Compatibilidad prevista

- Netflix publica los informes semestralmente y los describe como cobertura de aproximadamente 99% del tiempo de visualización.
- El informe de enero–junio de 2023 contiene horas vistas, fecha de estreno para títulos de Netflix y disponibilidad global.
- A partir de julio–diciembre de 2023, Netflix indica que añadió duración, visualizaciones (horas vistas divididas entre duración) y separación entre películas y series.
- Por ello, las tendencias de horas vistas podrán considerar los cinco periodos; los análisis de visualizaciones, duración y tipo de contenido comenzarán en 2023 H2. Esta regla se validará contra los encabezados reales de cada libro antes de cualquier cálculo.

No se usarán resultados analíticos provenientes de una fuente que no figure aquí.
