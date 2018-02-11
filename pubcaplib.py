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
        if buscaeventos.text == "Capitulos de libro":
            all = a
            #print(all)
            break
    except AttributeError:
        pass
if all != 0:
    containerb = containers[all]
    container = containerb.findAll("blockquote")
    f = open ("./Resultados/Publicaciones.csv", "a")
    for x in range(0, len(container)):
        cont = container[x]
        info_evento = cont.text
        index1 = info_evento.find(',                    \r\n                            \r\n\r\n                            "') + 84
        index2 = info_evento.find('"\r\n                            ')
        NombreProducto = info_evento[index1:index2]
        index1 = info_evento.find("ISBN:") + 6
        index2 = info_evento.find("\xa0\r\n                            ed:")
        ISSN = info_evento[index1:index2]
        index = info_evento.find(',                    \r\n                            \r\n\r\n                            "') + 84
        index1 = info_evento.find("\r\n                    ", index , len(info_evento)) + 30
        index2 = info_evento.find('\r\n                            . En:')
        Editorial = info_evento[index1:index2]
        index1 = info_evento.find('\xa0\r\n                            \r\n                            ,') + 62
        index2 = index1 + 4
        AnoEvento = info_evento[index1:index2]
        f.write("Capítulos de Libros" + ";" \
        + "-" + ";" \
        + ISSN.strip().replace("\r\n","") + ";" \
        + "-" + ";" \
        + Editorial.strip().replace("\r\n","").replace(";" , "|") + ";" \
        + "-" + ";" \
        + AnoEvento.strip().replace("\r\n","") + ";" \
        + "Sin Información" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + NombreProducto.strip().replace("\r\n","").replace(";" , "|") + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" + ";" \
        + "-" \
        + "\n")
        p = 0
    f.close()
else:
    print("El Docente no tiene Capítulos de libros Asociados")
