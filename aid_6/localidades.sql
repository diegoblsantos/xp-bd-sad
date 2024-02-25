create external table localidades (
	LOCALIDADE_ID int, 
	CIDADE string,
	ESTADO string,
	PAIS_ID int
)
row format delimited 
fields terminated by ',' 
lines terminated by '\n' 
location '/xp/bd/rh/localidades/'
TBLPROPERTIES ("skip.header.line.count"="1");