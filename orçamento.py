#Projeto: Manipulando Planilhas Excel

from openpyxl import Workbook
orcamento = Workbook()

Novembro = orcamento.active 

Novembro["A1"] = "Contas"
Novembro["B1"] = "Receitas"
Novembro["C1"] = "Despesas"
Novembro["D1"] = "Resultados"

Novembro["A2"] = "Alimentação"
Novembro["A3"] = "Energia"
Novembro["A4"] = "Transporte"

Novembro["B2"] = 1000
Novembro["C2"] = 200
Novembro["C3"] = 200
Novembro["C4"] = 200
Novembro["D2"] = Novembro["B2"].value - (Novembro["C2"].value + Novembro["C3"].value + Novembro["C4"].value) 

orcamento.save("orcamento.xlsx")
