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
from openpyxl import load_workbook
#Definitions
my_url = \
'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001333865'
wb = load_workbook('./Base.xlsx')

import init

import eventos
import pubeven
import pubarti
import publib
import pubcaplib
import pubsoft

print ("Done! :]")
