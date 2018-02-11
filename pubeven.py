#
#
# #############################################################################
#         Copyright (c) 2018 by Manuel Embus. All Rights Reserved.
#
#             This work is licensed under a Creative Commons
#       Attribution - NonCommercial - ShareAlike 4.0
#       International License.
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
# #############################################################################
#
#
from main import my_url
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
all = 0
a = 0
x = 0
y = 0
a
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("table")
for a in range(0,len(containers)):
    buscaeventos = containers[a].h3
    #print(buscaeventos)
    try:
        if buscaeventos.text == "Eventos científicos":
            all = a
            print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("table")
f = open ("./Resultados/Publicaciones_Eventos.csv", "w")
headers = "Tipo_Producto; \
Nombre_Producto;\
ISBN/ISSN; \
Tipo_Obra; \
Publicado_en; \
País; \
Año; \
Idioma; \
Volumen; \
Página; \
Nombre_del_Capítulo; \
Carácter; \
Idioma_Destino; \
Entidad; \
Número/Código_Registro; \
Observaciones_Extra\n"
f.write(headers)
for x in range(0, len(container)):
    cont = container[x]
    info_evento = cont.td.text
    index1 = info_evento.find("Nombre del evento:") + 18
    index2 = info_evento.find("Tipo de evento:")
    NombreEvento = info_evento[index1:index2]
    index1 = info_evento.find("Realizado el:") + 13
    index2 = index1 + 4
    AnoEvento = info_evento[index1:index2]
    if AnoEvento == ",&nbsp":
        AnoEvento = "-"
    index1 = info_evento.find(" \xa0\r\n                                            en ") + 51
    index2 = info_evento.find(" \xa0 -  \xa0\r\n")
    LugarEvento = info_evento[index1:index2]
    b_productos = cont.findAll("td")
    productos = b_productos[1].findAll("li")
    for y in range(0, len(productos)):
        prod = productos[y].text
        index1 = prod.find("Nombre del producto:") + 20
        index2 = prod.find("Tipo de producto:")
        NombreProducto = prod[index1:index2]
        index1 = prod.find("Tipo de producto:") + 17
        index2 = prod.find(") -") + 1
        Tipopub = prod[index1:index2]
        if Tipopub == "Producción bibliográfica - Trabajos en eventos (Capítulos de memoria)":
            Tipopub = "Capítulos de memoria"
        f.write(Tipopub.strip().replace("\n","") + ";" \
        + NombreProducto.replace("\r\n","").replace("\n","").strip().replace(";" , "|") + ";" \
        + "-".replace("\n","") + ";" \
        + "-".replace("\n","") + ";" \
        + NombreEvento.strip().replace("\r\n","").replace(";" , "|") + ";" \
        + LugarEvento.strip().replace("\r\n","").replace(";" , "|") + ";" \
        + AnoEvento.strip() + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" \
        + "\n")
    p = 0
f.close()
