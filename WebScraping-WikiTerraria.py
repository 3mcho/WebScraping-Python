import requests
from lxml import html
from bs4 import BeautifulSoup
import csv


#Navegador y la url
cadena ="Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0"
url= "https://terraria.fandom.com/es/wiki/Armaduras"

encabezados = {'user-agent':cadena}
pagina = requests.get(url, headers=encabezados)

analizador1=BeautifulSoup(pagina.text, "html.parser")
#print(analizador1.text)
analizador2 = html.fromstring(str(analizador1))

tabla = analizador2.find_class("article-table")

# Lista para almacenar los datos
datos_tabla = []

# Extraer filas y celdas de la tabla
for fila in tabla[0].xpath(".//tr"):
    fila_datos = [celda.text_content().strip() for celda in fila.xpath(".//td")]
    if fila_datos:  # Ignorar filas vacía
        datos_tabla.append(fila_datos)


# Escribir los datos en un archivo CSV
nombre_archivo = "tabla_armaduras.csv"
with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    # Escribir las filas de datos en el archivo CSV
    escritor_csv.writerows(datos_tabla)

print(f"Datos guardados en {nombre_archivo}")