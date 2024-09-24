desc;

SELECT
	*
FROM
	information_schema.schemata;
	
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










