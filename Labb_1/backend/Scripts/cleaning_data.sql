-- visa data för genomsnittlig visningslängd
SELECT *
FROM datum.tabelldata
LIMIT 10;

-- kollar efter nullvärden 
SELECT COUNT(*) AS Nullvardes_Rader
FROM datum.tabelldata
WHERE Visningar IS NULL
   OR "Visningstid (timmar)" IS NULL
   OR "Genomsnittlig visningslängd" IS NULL;
  
-- rensar och behåller viktiga kolumner med avrundning av decimaler och skapar tabell. 
CREATE TABLE cleaned_tabelldata_new AS
SELECT 
    Datum, 
    Visningar, 
    ROUND("Visningstid (timmar)", 2) AS "Visningstid (timmar)"
FROM datum.tabelldata
WHERE Visningar IS NOT NULL
  AND "Visningstid (timmar)" IS NOT NULL
  AND Datum != 'Totalt';

-- tittar på datan efter rensning.
 SELECT *
FROM cleaned_tabelldata_new;

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






 


