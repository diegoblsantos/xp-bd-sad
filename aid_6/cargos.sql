create external table cargos (
	CARGO_ID string, 
	NOME_CARGO string
)
row format delimited 
fields terminated by ',' 
lines terminated by '\n' 
location '/xp/bd/rh/cargos/'
TBLPROPERTIES ("skip.header.line.count"="1");