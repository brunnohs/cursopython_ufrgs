#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""

Projeto Final da Extensão - Introdução ao Python
Descrição: Trata-se de um projeto que realiza as ações descritas a segur:
a) Cria a pasta "Pasta Python"
b) Cria os arquivos Despesas Correntes.xlsx, Despesas Correntes.docx, Despesas Capital.xlsx, Despesas Capital.docx e Relatório.docx e os insere na pasta "Pasta Python"
c) Cria as subpastas "Planilhas" e "Documentos"
d) Transfere os arquivos de extensão xlsx. para a subpasta "Planilhas" e os arquivo de extensão docx. para a subpasta "Documentos"
Autor: Brunno Henrique Sibin
Data: 03/12/2022
Versão: 0.0.2

"""

import os
import shutil

#1. Definir o diretório inicial e criar a pasta "Pasta Python"

diretorio="C:\\Users\\Bruno\\Desktop"
os.chdir(str(diretorio))
pasta_python="Pasta Python/"
if (not os.path.exists(pasta_python)):
    os.mkdir(pasta_python)

#2. Criar os arquivos .xlsx e .docx dentro da "Pasta Python"

pasta_python="C:\\Users\\Bruno\\Desktop\\Pasta Python"
os.chdir(str(pasta_python))
with open("DespesasCorrentes.xlsx","w") as arquivo_1:
    arquivo_1.write("Despesas Correntes")
with open("DespesasCorrentes.docx","w") as arquivo_2:
    arquivo_2.write("Despesas Correntes")
with open("DespesasCapital.xlsx","w") as arquivo_3:
    arquivo_3.write("Despesas Capital")
with open("DespesasCapital.docx","w") as arquivo_4:
    arquivo_4.write("Despesas Capital")
with open("Relatorio.docx","w") as arquivo_5:
    arquivo_5.write("Relatorio")    
    
#3. Criar as subpastas "Documentos" e "Planilhas" dentro da pasta "Pasta Python"

documentos="Documentos/"
if (not os.path.exists(documentos)):
    os.mkdir(documentos)

planilhas="Planilhas/"
if (not os.path.exists(planilhas)):
    os.mkdir(planilhas)
    
#4. Transferir os arquivos .xlsx e .docx. para as pastas "Planilhas" (se for .xlsx) e "Documentos" (se for .docx)

os.rename("DespesasCorrentes.xlsx","Planilhas\\DespesasCorrentes.xlsx")
os.rename("DespesasCorrentes.docx","Documentos\\DespesasCorrentes.docx")
os.rename("DespesasCapital.xlsx","Planilhas\\DespesasCapital.xlsx")
os.rename("DespesasCapital.docx","Documentos\\DespesasCapital.docx")        
os.rename("Relatorio.docx","Documentos\\Relatorio.docx") 


# In[ ]:




