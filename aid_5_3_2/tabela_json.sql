CREATE EXTERNAL TABLE ibge_json
(
nome string,
regiao int,
freq int,
rank int,
sexo string
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.contrib.serde2.JsonSerde'
location '/xp/bd/ibge/json';