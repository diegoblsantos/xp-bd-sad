create external table cidades (estado string, sigla string, nome string)
row format delimited 
fields terminated by ';' 
lines terminated by '\n' 
location '/xp/bd/'
TBLPROPERTIES ("skip.header.line.count"="1");