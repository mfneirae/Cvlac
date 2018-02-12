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

import openpyxl
wb = openpyxl.load_workbook('./Base.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
total = sheet.max_row
print("total: ",total)
import init
init.inicio()
for x in range(2,total):
    doc = sheet['A'+str(x)].value
    name = sheet['B'+str(x)].value
    last = sheet['C'+str(x)].value
    my_url = sheet['E'+str(x)].value
    depar = sheet['D'+str(x)].value
    print("For en:",x)
    if my_url != '-':
        import eventos
        eventos.evenextract()
        # import pubeven
        # import pubarti
        # import publib
        # import pubcaplib
        # import pubsoft
    else:
        pass

f = open ("./Resultados/Eventos.csv", "a")
for item in init.dbact:
  f.write(item)
f.close()
print ("Done! :]")
