# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 16:32:20 2024

@author: Diego Bernardes
"""

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

caminho_entrada = "<caminho>/nomes-ibge.csv"
caminho_saida = "<caminho>/nomes-ibge.parquet"

# Ler o arquivo CSV
df = pd.read_csv(caminho_entrada, encoding="utf-8")

print(df.head())

# Escrever o DataFrame em um arquivo Parquet
pq.write_table(pa.Table.from_pandas(df), caminho_saida)
