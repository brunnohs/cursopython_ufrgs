#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil

pasta_original = "C:\\Users\\Bruno\\Desktop\\Python"
documentos = "C:\\Users\\Bruno\\Desktop\\Python\\documentos"
planilhas = "C:\\Users\\Bruno\\Desktop\\Python\\planilhas"

os.chdir(str(pasta_original))

os.rename("DespesasCorrentes.xlsx","planilhas\\DespesasCorrentes.xlsx")
os.rename("DespesasCorrentes.docx","documentos\\DespesasCorrentes.docx")
os.rename("DespesasCapital.xlsx","planilhas\\DespesasCapital.xlsx")
os.rename("DespesasCapital.docx","documentos\\DespesasCapital.docx")        
os.rename("relatorio.docx","documentos\\relatorio.docx")    


# In[2]:





# In[ ]:




