CREATE EXTERNAL TABLE ibge_orc
(
nome string,
regiao int,
freq int,
rank int,
sexo string
) 
STORED AS PARQUET
location '/xp/bd/ibge/parquet';