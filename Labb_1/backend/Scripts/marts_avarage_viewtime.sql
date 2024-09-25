desc;

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

CREATE TABLE IF NOT EXISTS marts.genomsnittlig_visningslangd AS
SELECT *
FROM cleaned_tabelldata_new;


SELECT *
FROM information_schema.tables
WHERE table_schema = 'marts';

SELECT * FROM marts.genomsnittlig_visningslangd;