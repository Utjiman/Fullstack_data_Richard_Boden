desc;

SELECT
	*
FROM
	information_schema.schemata;
	
-- skapar schemat
CREATE SCHEMA IF NOT EXISTS marts;

-- Lägger in de tre rensade tabellerna i marts-shcemat
CREATE TABLE marts.total_visningar_per_dag AS
SELECT *
FROM cleaned_total_visningar_per_dag;


CREATE TABLE marts.genomsnittlig_visningslangd AS
SELECT *
FROM cleaned_tabelldata_new;


CREATE TABLE marts.visningar_per_enhetstyp AS
SELECT *
FROM cleaned_visningar_per_enhetstyp;



-- kontrollerar att dom finns i marts-schemat.
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'marts';


SELECT * FROM marts.visningar_per_enhetstyp;

SELECT * FROM marts.genomsnittlig_visningslangd;

SELECT * FROM marts.total_visningar_per_dag;








