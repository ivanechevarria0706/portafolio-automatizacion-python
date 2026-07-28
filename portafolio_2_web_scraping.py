"""
PORTAFOLIO - Ejemplo 2: Web Scraping de Productos
===================================================

Qué problema resuelve:
Negocios que quieren monitorear precios/listados de otros sitios (competencia,
proveedores, portales de empleo, etc.) sin copiar todo a mano.

Este ejemplo extrae datos de "books.toscrape.com", un sitio público diseñado
específicamente para practicar scraping (no requiere permisos ni riesgo legal,
ideal para mostrar en portafolio). La misma lógica se adapta a sitios reales:
solo cambian los selectores HTML.

Qué extrae:
- Título del producto
- Precio
- Disponibilidad
- Rating (calificación en estrellas)

Cómo usarlo:
    pip install requests beautifulsoup4 pandas
    python portafolio_2_web_scraping.py

Salida: "productos_extraidos.csv" con todos los datos listos para abrir en Excel.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
MAX_PAGINAS = 3  # Ajustable: cuántas páginas quieres extraer
ARCHIVO_SALIDA = "productos_extraidos.csv"

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def extraer_pagina(pagina: int) -> list[dict]:
    """Extrae los productos de una página del catálogo."""
    url = BASE_URL.format(pagina)
    respuesta = requests.get(url, timeout=10)

    if respuesta.status_code != 200:
        print(f"  Página {pagina} no disponible (status {respuesta.status_code}), deteniendo.")
        return []

    soup = BeautifulSoup(respuesta.text, "html.parser")
    productos = []

    for item in soup.select("article.product_pod"):
        titulo = item.h3.a["title"]
        precio = item.select_one(".price_color").text.strip()
        disponibilidad = item.select_one(".availability").text.strip()
        clase_rating = item.select_one(".star-rating")["class"][1]  # ej: "Three"
        rating = RATING_MAP.get(clase_rating, None)

        productos.append({
            "titulo": titulo,
            "precio": precio,
            "disponibilidad": disponibilidad,
            "rating_estrellas": rating,
        })

    return productos


def main():
    print("=== Iniciando extracción de datos ===\n")
    todos_los_productos = []

    for pagina in range(1, MAX_PAGINAS + 1):
        print(f"Extrayendo página {pagina}/{MAX_PAGINAS}...")
        productos = extraer_pagina(pagina)
        if not productos:
            break
        todos_los_productos.extend(productos)
        time.sleep(1)  # Buena práctica: no saturar el servidor

    df = pd.DataFrame(todos_los_productos)
    df.to_csv(ARCHIVO_SALIDA, index=False, encoding="utf-8-sig")

    print(f"\n✅ Extracción completa: {len(df)} productos guardados en '{ARCHIVO_SALIDA}'")
    print("\nVista previa:")
    print(df.head())


if __name__ == "__main__":
    main()
