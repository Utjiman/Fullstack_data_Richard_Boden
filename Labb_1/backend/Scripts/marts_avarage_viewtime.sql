desc;

CREATE TABLE IF NOT EXISTS marts.genomsnittlig_visningslangd AS
SELECT *
FROM cleaned_tabelldata_new;


SELECT *
FROM information_schema.tables
WHERE table_schema = 'marts';

SELECT * FROM marts.genomsnittlig_visningslangd;