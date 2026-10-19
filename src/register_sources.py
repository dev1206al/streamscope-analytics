"""Genera un manifiesto reproducible para los libros fuente oficiales de Netflix."""

from __future__ import annotations

import argparse
import csv
import hashlib
from datetime import date
from pathlib import Path

import pandas as pd


SOURCES = {
    "What_We_Watched_A_Netflix_Engagement_Report_2023Jan-Jun.xlsx": {
        "source_id": "NFLX_WWW_2023_H1",
        "period": "2023 H1 (Jan-Jun)",
        "source_url": "https://assets.ctfassets.net/4cd45et68cgf/1HyknFM84ISQpeua6TjM7A/97a0a393098937a8f29c9d29c48dbfa8/What_We_Watched_A_Netflix_Engagement_Report_2023Jan-Jun.xlsx",
    },
    "What_We_Watched_A_Netflix_Engagement_Report_2023Jul-Dec.xlsx": {
        "source_id": "NFLX_WWW_2023_H2",
        "period": "2023 H2 (Jul-Dec)",
        "source_url": "https://assets.ctfassets.net/4cd45et68cgf/inuAnzotdsAEgbInGLzH5/1be323ba419b2af3a96bffa29acc31a3/What_We_Watched_A_Netflix_Engagement_Report_2023Jul-Dec.xlsx",
    },
    "What_We_Watched_A_Netflix_Engagement_Report_2024Jan-Jun.xlsx": {
        "source_id": "NFLX_WWW_2024_H1",
        "period": "2024 H1 (Jan-Jun)",
        "source_url": "https://assets.ctfassets.net/4cd45et68cgf/2PoZlfdc46dH2gQvI8eUzI/9db5840720c47acfcf7b89ffe2402860/What_We_Watched_A_Netflix_Engagement_Report_2024Jan-Jun.xlsx",
    },
    "What_We_Watched_A_Netflix_Engagement_Report_2024Jul-Dec.xlsx": {
        "source_id": "NFLX_WWW_2024_H2",
        "period": "2024 H2 (Jul-Dec)",
        "source_url": "https://assets.ctfassets.net/4cd45et68cgf/6XSmoEjBjVMPRtYybT9d1E/8c0b0b2645b8712d5597b0bdbe0d64e2/What_We_Watched_A_Netflix_Engagement_Report_2024Jul-Dec.xlsx",
    },
    "What_We_Watched_A_Netflix_Engagement_Report_2025Jan-Jun.xlsx": {
        "source_id": "NFLX_WWW_2025_H1",
        "period": "2025 H1 (Jan-Jun)",
        "source_url": "https://assets.ctfassets.net/4cd45et68cgf/mplcXj5ulHDfbCPCr0f0I/5dbb6ec09f03df89706476e380e9b8bd/What_We_Watched_A_Netflix_Engagement_Report_2025Jan-Jun.xlsx",
    },
}


def sha256(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as source_file:
        for block in iter(lambda: source_file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def profile_workbook(file_path: Path) -> tuple[int, str, str]:
    """Devuelve filas de datos, conteos por hoja y encabezados detectados."""
    workbook = pd.ExcelFile(file_path)
    sheet_counts: list[str] = []
    sheet_headers: list[str] = []
    total_rows = 0

    for sheet_name in workbook.sheet_names:
        raw_frame = pd.read_excel(workbook, sheet_name=sheet_name, header=None)
        header_index = next(
            (
                index
                for index, row in raw_frame.iterrows()
                if "Title" in {str(value).strip() for value in row.dropna()}
            ),
            None,
        )
        if header_index is None:
            raise ValueError(
                f"No se encontró una fila de encabezados con 'Title' en {file_path.name}"
            )

        frame = pd.read_excel(workbook, sheet_name=sheet_name, header=header_index)
        frame = frame.loc[:, ~frame.columns.astype(str).str.startswith("Unnamed:")]
        frame = frame.dropna(subset=["Title"])
        row_count = len(frame.index)
        total_rows += row_count
        sheet_counts.append(f"{sheet_name}: {row_count}")
        headers = ", ".join(str(column) for column in frame.columns)
        sheet_headers.append(f"{sheet_name}: {headers}")

    return total_rows, " | ".join(sheet_counts), " | ".join(sheet_headers)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Registra los libros oficiales de Netflix What We Watched."
    )
    parser.add_argument(
        "--downloaded-on",
        default=date.today().isoformat(),
        help="Fecha de descarga de los archivos, en formato AAAA-MM-DD.",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("data/raw"),
        help="Directorio que contiene los archivos XLSX fuente.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/source_manifest.csv"),
        help="Ruta para el manifiesto de fuentes generado.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        date.fromisoformat(args.downloaded_on)
    except ValueError as error:
        raise SystemExit("--downloaded-on debe usar el formato AAAA-MM-DD.") from error

    rows: list[dict[str, str | int]] = []
    missing_files: list[str] = []
    for filename, source in SOURCES.items():
        file_path = args.raw_dir / filename
        if not file_path.is_file():
            missing_files.append(filename)
            continue

        total_rows, rows_by_sheet, headers_by_sheet = profile_workbook(file_path)
        rows.append(
            {
                **source,
                "filename": filename,
                "downloaded_on": args.downloaded_on,
                "file_size_bytes": file_path.stat().st_size,
                "sha256": sha256(file_path),
                "total_data_rows": total_rows,
                "rows_by_sheet": rows_by_sheet,
                "headers_by_sheet": headers_by_sheet,
            }
        )

    if missing_files:
        raise SystemExit("Faltan archivos fuente esperados: " + ", ".join(missing_files))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with args.output.open("w", newline="", encoding="utf-8") as manifest:
        writer = csv.DictWriter(manifest, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Se registraron {len(rows)} libros en {args.output}.")


if __name__ == "__main__":
    main()
