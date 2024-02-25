# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:07:33 2024

@author: Diego Bernardes
"""

import pandas as pd
import pyarrow as pa
import pyarrow.orc as orc

def csv_to_orc(csv_file, orc_file):
    # Lê o arquivo CSV usando o pandas
    df = pd.read_csv(csv_file)
    
    # Escreve o DataFrame no arquivo ORC usando o pyarrow
    table = pa.Table.from_pandas(df)
    with pa.OSFile(orc_file, 'wb') as sink:
        orc.write_table(table, sink)

# Exemplo de utilização
csv_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_2_2/nomes-ibge.csv"
orc_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_2_2/nomes-ibge.orc"

# Converte o arquivo CSV para ORC
csv_to_orc(csv_file, orc_file)
