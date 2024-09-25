desc;

SELECT
	*
FROM
	information_schema.schemata;


-- tittar på datan för enhetstyper 
SELECT *
FROM enhetstyp.tabelldata
LIMIT 10;

-- tittar efter nullvärden.
SELECT 
    COUNT(*) AS Null_Vardes_Enhetstyp,
    SUM(CASE WHEN Visningar IS NULL THEN 1 ELSE 0 END) AS Null_Vardes_Visningar,
    SUM(CASE WHEN "Visningstid (timmar)" IS NULL THEN 1 ELSE 0 END) AS Null_Vardes_Visningstid
FROM enhetstyp.tabelldata;

-- rensar bort nullvärden och tar bort summeringsraden "totalt" och skapar tabell.
CREATE TABLE cleaned_visningar_per_enhetstyp AS
SELECT 
    Enhetstyp, 
    Visningar, 
    ROUND("Visningstid (timmar)", 2) AS "Visningstid (timmar)"
FROM enhetstyp.tabelldata
WHERE Enhetstyp IS NOT NULL  -- Exkludera rader där Enhetstyp är null
  AND Enhetstyp != 'Totalt'  -- Exkludera raden med Totalt
  AND Visningar IS NOT NULL
  AND "Visningstid (timmar)" IS NOT NULL;
 
 SELECT * FROM cleaned_visningar_per_enhetstyp;



-- skapar schemat
CREATE SCHEMA IF NOT EXISTS marts;

-- Lägger in de rensade tabellerna i marts-shcemat

CREATE TABLE IF NOT EXISTS marts.visningar_per_enhetstyp AS
SELECT *
FROM cleaned_visningar_per_enhetstyp;



-- kontrollerar att dom finns i marts-schemat.
SELECT *
FROM information_schema.tables
WHERE table_schema = 'marts';


SELECT * FROM marts.visningar_per_enhetstyp;










