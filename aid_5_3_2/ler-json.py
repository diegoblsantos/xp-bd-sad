# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:11:32 2024

@author: Diego Bernardes
"""

import pandas as pd

def print_json_as_table(json_file):
    # Carrega o arquivo JSON em um DataFrame do pandas
    df = pd.read_json(json_file)
    
    # Imprime os dados na tela
    print(df)

# Nome do arquivo JSON
json_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_3_2/nomes-ibge.json"

# Chama a função para ler o arquivo JSON e imprimir como tabela
print_json_as_table(json_file)
