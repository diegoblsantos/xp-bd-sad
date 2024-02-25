create external table paises (
	PAIS_ID int, 
	PAIS_NOME string,
	REGIAO_ID int
)
row format delimited 
fields terminated by ',' 
lines terminated by '\n' 
location '/xp/bd/rh/paises/'
TBLPROPERTIES ("skip.header.line.count"="1");