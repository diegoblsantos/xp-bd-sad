# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 16:43:33 2024

@author: Diego Bernardes
"""

import pyarrow.parquet as pq

caminho_parquet = "<caminho>/nomes-ibge.parquet"

# Ler o arquivo Parquet
table = pq.read_table(caminho_parquet)

# Converter a tabela em um DataFrame do pandas e imprimir na tela
df = table.to_pandas()


print(df)
