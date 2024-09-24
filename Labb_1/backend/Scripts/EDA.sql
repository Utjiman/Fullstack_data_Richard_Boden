WITH 
	date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
	STRFTIME('%Y-%m-%d', tot.datum), 
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM date_total as tot
LEFT JOIN date_table as tab 
ON tot.datum = tab.datum;



SELECT Enhetstyp, count(*) total_rows, sum(Visningar) as total_visningar 
from 
enhetstyp.diagramdata group by Enhetstyp ;

select * from enhetstyp.diagramdata d ;

SELECT * EXCLUDE (Innehåll) FROM  innehall.tabelldata ORDER BY "Visningstid (timmar)" DESC OFFSET 1 LIMIT 5;

SELECT * FROM  innehall.diagramdata;-- ORDER BY "Visningstid (timmar)";

SELECT STRFTIME('%Y-%m-%d', Datum), Visningar FROM innehall.totalt;



-- lista alla tabeller och respektive scheman
SELECT
	table_schema,
	table_name
FROM
	information_schema.tables;

-- Visar att date är datatypen för datum. BIGINT är datatypen för visningar båda kolumnerna kan tillåter NULL-värden.
DESCRIBE enhetstyp.totalt;

-- visar visningar per dag i fallande ordning. visningar varierar dag för dag.
SELECT
	Datum,
	Visningar
FROM
	enhetstyp.totalt
ORDER BY
	Visningar DESC;

-- kollar efter saknade data. Ingen data saknas.
SELECT
	*
FROM
	enhetstyp.totalt
WHERE
	Visningar IS NULL;

-- vilken enhetstyp som genererar mest visningar.
SELECT
	Enhetstyp,
	SUM(Visningar) AS Total_Visningar
FROM
	enhetstyp.tabelldata
GROUP BY
	Enhetstyp
ORDER BY
	Total_Visningar DESC;

-- Varchar, Bigint, double och time datatyper.
DESCRIBE Operativsystem.tabelldata;

-- Listar visningar per os. Denna kan behöva rensas lite om den ska användas.
SELECT
	* 
from
	operativsystem.tabelldata;

