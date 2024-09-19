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

