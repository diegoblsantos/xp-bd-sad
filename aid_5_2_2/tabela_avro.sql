CREATE TABLE ibge_avro
ROW FORMAT SERDE
'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
location '/xp/bd/ibge/avro/'
TBLPROPERTIES (
 'avro.schema.literal'='{
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
 }'
 );