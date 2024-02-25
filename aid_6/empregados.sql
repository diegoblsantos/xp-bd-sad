create external table empregados (
	EMPREGADO_ID int, 
	NOME string, 
	SOBRENOME string, 
	EMAIL string, 
	CARGO_ID string, 
	SALARIO decimal(10,2), 
	GERENTE_ID string, 
	DEPARTAMENTO_ID int
)
row format delimited 
fields terminated by ',' 
lines terminated by '\n' 
location '/xp/bd/rh/empregados/'
TBLPROPERTIES ("skip.header.line.count"="1");