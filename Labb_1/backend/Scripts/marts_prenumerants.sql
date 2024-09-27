SELECT * FROM prenumerationsstatus.tabelldata;


CREATE TABLE cleaned_prenumerationsstatus AS
SELECT Prenumerationsstatus, 
       SUM(Visningar) AS Total_Visningar, 
       ROUND(SUM("Visningstid (timmar)"), 2) AS Total_Visningstid
FROM prenumerationsstatus.tabelldata
WHERE Prenumerationsstatus != 'Totalt'  -- Tar bort "Totalt"-raden
GROUP BY Prenumerationsstatus
ORDER BY Total_Visningar DESC;

SELECT * FROM cleaned_prenumerationsstatus;

CREATE TABLE IF NOT EXISTS marts.cleaned_prenumerants  AS
SELECT *
FROM cleaned_prenumerationsstatus;

SELECT *
FROM information_schema.tables
WHERE table_schema = 'marts';


