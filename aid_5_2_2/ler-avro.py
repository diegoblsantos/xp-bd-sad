# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 18:48:00 2024

@author: Diego Bernardes
"""

from avro import datafile, io

def avro_to_stdout(avro_file):
    # Abre o arquivo Avro
    with open(avro_file, 'rb') as f:
        # Cria um leitor Avro
        reader = datafile.DataFileReader(f, io.DatumReader())
        
        # Itera sobre os registros no arquivo Avro
        for record in reader:
            # Imprime o registro na tela
            print(record)
        
        # Fecha o leitor Avro
        reader.close()

# Exemplo de utilização
avro_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_2_2/nomes-ibge.avro"

# Chama a função para ler o arquivo Avro e imprimir os dados na tela
avro_to_stdout(avro_file)
