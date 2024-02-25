CREATE EXTERNAL TABLE ibge_json
(
nome string,
regiao int,
freq int,
rank int,
sexo string
) 
ROW FORMAT SERDE 'org.apache.hcatalog.data.JsonSerDe'
location '/xp/bd/ibge/json';