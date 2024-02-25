create external table departamentos (
	DEPARTAMENTO_ID int, 
	DEPARTAMENTO_NOME string,
	LOCALIDADE_ID int
)
row format delimited 
fields terminated by ',' 
lines terminated by '\n' 
location '/xp/bd/rh/departamentos/'
TBLPROPERTIES ("skip.header.line.count"="1");