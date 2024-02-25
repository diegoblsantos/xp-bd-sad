create external table regioes (
	REGIAO_ID int, 
	REGIAO_NOME string
)
row format delimited 
fields terminated by ',' 
lines terminated by '\n' 
location '/xp/bd/rh/regioes/'
TBLPROPERTIES ("skip.header.line.count"="1");