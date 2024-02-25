CREATE EXTERNAL TABLE ibge_json
(
nome string,
regiao int,
freq int,
rank int,
sexo string
) 
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
location '/xp/bd/ibge/json';