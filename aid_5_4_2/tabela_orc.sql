CREATE EXTERNAL TABLE ibge_orc
(
nome string,
regiao int,
freq int,
rank int,
sexo string
) 
STORED AS ORC
location '/xp/bd/ibge/ibge_orc';