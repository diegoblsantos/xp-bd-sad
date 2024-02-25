# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:07:15 2024

@author: Diego Bernardes
"""

import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    # Lê o arquivo CSV
    data = pd.read_csv(csv_file)
    
    # Converte os dados para um dicionário
    data_dict = data.to_dict(orient='records')
    
    # Salva os dados em um arquivo JSON
    with open(json_file, 'w') as f:
        json.dump(data_dict, f, indent=4)

# Nome do arquivo CSV de entrada
csv_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_3_2/nomes-ibge.csv"

# Nome do arquivo JSON de saída
json_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_3_2/nomes-ibge.json"

# Chama a função para converter CSV para JSON
csv_to_json(csv_file, json_file)

print("Dados convertidos de CSV para JSON com sucesso!")
