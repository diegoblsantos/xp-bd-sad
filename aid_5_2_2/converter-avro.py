import csv
from avro import schema, datafile, io

def csv_to_avro(csv_file, avro_file, schema_dict):
    # Define o esquema Avro
    avro_schema = schema.parse(schema_dict)

    # Abre o arquivo CSV
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Abre o arquivo Avro
        with open(avro_file, 'wb') as out:
            # Cria um escritor Avro
            writer = datafile.DataFileWriter(out, io.DatumWriter(), avro_schema)
            
            # Itera sobre as linhas do arquivo CSV
            for row in reader:
                # Escreve a linha no arquivo Avro
                writer.append(row)
            
            # Fecha o escritor Avro
            writer.close()

# Exemplo de utilização

csv_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_2_2/nomes-ibge.csv"
avro_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_2_2/nomes-ibge.avro"
avro_schema_file = "D:/IGTI/Banco de Dados em Arquivos/repositorio/xp-bd-sad/aid_5_2_2/schema_nomes.avsc"

# Esquema Avro correspondente aos dados do CSV
avro_schema = """
{
    "type": "record",
    "name": "nomes_ibge",
	"namespace": "default",
    "fields": [
        {"name": "nome", "type": "string"},
        {"name": "regiao", "type": "string"},
        {"name": "freq", "type": "string"},
        {"name": "rank", "type": "string"},
        {"name": "sexo", "type": "string"}
    ]
}
"""



# Converte o arquivo CSV para Avro
csv_to_avro(csv_file, avro_file, avro_schema)
