SELECT
	* 
from
	operativsystem.tabelldata;
	
-- skapar table för operativssystem
CREATE TABLE cleaned_operativsystem AS
SELECT 
    Operativsystem, 
    Visningar, 
    ROUND("Visningstid (timmar)", 2) AS "Visningstid (timmar)", 
    "Genomsnittlig visningslängd"
FROM operativsystem.tabelldata
WHERE Operativsystem != 'Totalt'   -- Exkludera raden med Totalt
  AND Visningar > 0  			   -- Exkludera rader med noll visningar
  AND "Visningstid (timmar)" > 0;  -- Exkludera rader med noll visningstid

SELECT * FROM cleaned_operativsystem;
  
 CREATE TABLE IF NOT EXISTS marts.cleaned_os  AS
SELECT *
FROM cleaned_operativsystem;

SELECT *
FROM information_schema.tables
WHERE table_schema = 'marts';