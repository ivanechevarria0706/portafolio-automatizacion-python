"""
PORTAFOLIO - Ejemplo 1: Automatización de Reportes
====================================================

Qué problema resuelve:
Muchas empresas reciben varios archivos Excel/CSV (por sucursal, por vendedor,
por mes) y alguien tiene que copiar y pegar todo a mano en un solo reporte.
Este script automatiza ese proceso: junta todos los archivos de una carpeta,
los combina en un solo reporte, calcula totales y genera un resumen.

Cómo usarlo:
1. Coloca tus archivos .csv o .xlsx dentro de la carpeta "datos_entrada/"
   (cada archivo debe tener las mismas columnas, ej: Fecha, Producto, Cantidad, Precio)
2. Ejecuta: python portafolio_1_automatizacion_reportes.py
3. Obtendrás "reporte_consolidado.xlsx" con:
   - Todos los datos juntos en una hoja
   - Un resumen de ventas totales por producto en otra hoja

Este es el tipo de script que se ofrece como servicio de
"automatización de Excel/Google Sheets" en Fiverr/Upwork.
"""

import pandas as pd
import os
from pathlib import Path
from datetime import datetime

CARPETA_ENTRADA = "datos_entrada"
ARCHIVO_SALIDA = "reporte_consolidado.xlsx"


def cargar_archivos(carpeta: str) -> pd.DataFrame:
    """Lee todos los .csv y .xlsx de una carpeta y los combina en un solo DataFrame."""
    archivos = list(Path(carpeta).glob("*.csv")) + list(Path(carpeta).glob("*.xlsx"))

    if not archivos:
        raise FileNotFoundError(
            f"No se encontraron archivos .csv o .xlsx en '{carpeta}'. "
            "Agrega tus archivos ahí antes de correr el script."
        )

    dataframes = []
    for archivo in archivos:
        print(f"Leyendo: {archivo.name}")
        if archivo.suffix == ".csv":
            df = pd.read_csv(archivo)
        else:
            df = pd.read_excel(archivo)
        df["archivo_origen"] = archivo.name
        dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)


def generar_resumen(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un resumen de totales por producto, asumiendo columnas Producto/Cantidad/Precio."""
    if not {"Producto", "Cantidad", "Precio"}.issubset(df.columns):
        print("Aviso: no se encontraron columnas 'Producto', 'Cantidad', 'Precio'. "
              "Se omite el resumen automático de ventas.")
        return pd.DataFrame()

    df["Total"] = df["Cantidad"] * df["Precio"]
    resumen = (
        df.groupby("Producto")
        .agg(unidades_vendidas=("Cantidad", "sum"), ingreso_total=("Total", "sum"))
        .sort_values("ingreso_total", ascending=False)
        .reset_index()
    )
    return resumen


def main():
    print("=== Iniciando consolidación de reportes ===\n")

    if not os.path.exists(CARPETA_ENTRADA):
        os.makedirs(CARPETA_ENTRADA)
        print(f"Se creó la carpeta '{CARPETA_ENTRADA}/'. Coloca ahí tus archivos y vuelve a correr el script.")
        return

    datos_completos = cargar_archivos(CARPETA_ENTRADA)
    resumen = generar_resumen(datos_completos)

    with pd.ExcelWriter(ARCHIVO_SALIDA, engine="openpyxl") as writer:
        datos_completos.to_excel(writer, sheet_name="Datos completos", index=False)
        if not resumen.empty:
            resumen.to_excel(writer, sheet_name="Resumen por producto", index=False)

    print(f"\n✅ Reporte generado: {ARCHIVO_SALIDA}")
    print(f"   Filas totales combinadas: {len(datos_completos)}")
    print(f"   Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    main()
