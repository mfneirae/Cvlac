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
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("table")
for a in range(0,len(containers)):
    buscaeventos = containers[a].h3
    #print(buscaeventos)
    try:
        if buscaeventos.text == "Artículos":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("blockquote")
f = open ("./Resultados/Publicaciones_Artículos.csv", "w")
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
    info_evento = cont.text
    index1 = info_evento.find('\r\n                    "') + 23
    index2 = info_evento.find('"\r\n                    . En:')
    NombreProducto = info_evento[index1:index2]
    index1 = info_evento.find("ISSN:") + 6
    index2 = index1 + 9
    ISSN = info_evento[index1:index2]
    index1 = info_evento.find("\xa0\r\n                    ") + 23
    index2 = info_evento.find("\xa0\r\n                    ISSN:")
    Revista = info_evento[index1:index2]
    index1 = info_evento.find("\r\n                    ,") + 23
    index2 = info_evento.find(",\r\n                    \xa0")
    AnoEvento = info_evento[index1:index2]
    index1 = info_evento.find("\nv.") + 3
    index2 = info_evento.find("\r\n                    fasc.")
    Volumen = info_evento[index1:index2]
    index1 = info_evento.find("\r\n                    p.") + 24
    index2 = info_evento.find("\r\n                    ,")
    Pag = info_evento[index1:index2]
    f.write("Artículo de revista" + ";" \
    + NombreProducto.strip().replace("\r\n","").replace(";" , "|") + ";" \
    + ISSN.strip().replace("\r\n","") + ";" \
    + "-" + ";" \
    + Revista.strip().replace("\r\n","").replace(";" , "|") + ";" \
    + "-" + ";" \
    + AnoEvento.strip().replace("\r\n","") + ";" \
    + "Sin Información" + ";" \
    + Volumen.replace("\r\n","").replace("\n","") + ";" \
    + "".join(Pag.replace("\r\n","").split()).replace("-"," a ") + ";" \
    + "-" + ";" \
    + "-" + ";" \
    + "-" + ";" \
    + "-" + ";" \
    + "-" + ";" \
    + "-" \
    + "\n")
    p = 0
f.close()
