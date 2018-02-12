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
#Eventos
f = open ("./Resultados/Actividades.csv", "w")
headers = "Departamento; \
Documento; \
Nombres; \
Apellidos; \
Observaciones; \
Tipo_Producto; \
Nombre_Producto_Asociado;\
Evento; \
Año; \
País; \
Ciudad; \
Financiación; \
Observaciones\n"
f.write(headers)
f.close()
#Publicaciones
f = open ("./Resultados/Publicaciones.csv", "w")
headers = "Departamento; \
Documento; \
Nombres; \
Apellidos; \
Observaciones; \
Tipo_Producto; \
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
f.close()
