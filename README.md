# Portafolio - Automatización y Scraping con Python

Colección de scripts que muestran cómo uso Python para resolver problemas
reales de negocio: ahorrar tiempo en tareas repetitivas y extraer datos
de la web de forma automática.

Disponible para proyectos freelance de automatización, scraping, bots y
análisis de datos. Contáctame por [https://www.fiverr.com/s/kLdee3w].

---

## 1. Automatización de Reportes (`portafolio_1_automatizacion_reportes.py`)

**Problema que resuelve:** empresas que reciben varios archivos Excel/CSV
(por sucursal, por vendedor, por mes) y necesitan combinarlos en un solo
reporte con totales, sin hacerlo a mano.

**Qué hace:**
- Lee todos los archivos `.csv` y `.xlsx` de una carpeta
- Los combina en un solo reporte
- Genera un resumen automático de ventas por producto
- Exporta todo a un archivo Excel con dos hojas (datos completos + resumen)

**Tecnologías:** `pandas`, `openpyxl`

**Cómo probarlo:**
```bash
pip install pandas openpyxl
python portafolio_1_automatizacion_reportes.py
```
Coloca tus archivos de entrada en una carpeta `datos_entrada/` antes de correrlo.
Si no tienes carpeta, al ejecuta el codigo por primera vez se crea la carpeta `datos_entrada/`

---

## 2. Web Scraping de Productos (`portafolio_2_web_scraping.py`)

**Problema que resuelve:** monitorear precios, listados o catálogos de
sitios web (competencia, proveedores, portales) sin copiar todo a mano.

**Qué hace:**
- Recorre varias páginas de un catálogo web
- Extrae título, precio, disponibilidad y calificación de cada producto
- Guarda todo en un archivo CSV listo para abrir en Excel

**Tecnologías:** `requests`, `BeautifulSoup`, `pandas`

**Cómo probarlo:**
```bash
pip install requests beautifulsoup4 pandas
python portafolio_2_web_scraping.py
```

> Nota: este ejemplo usa un sitio público diseñado para practicar scraping.
> La misma lógica se adapta a sitios reales cambiando los selectores HTML.

---

## Servicios que ofrezco

- Automatización de tareas repetitivas en Excel / Google Sheets
- Web scraping y extracción de datos
- Bots simples para Telegram / Discord
- Limpieza y análisis básico de datos con Python

**Contacto:** [agrega tu email o link de Fiverr/Upwork aquí]
