### Labb 1
setup a). Clonade repot och kopierade in 10_lab_overview in i mitt repo.

setup b). Lagt till i .gitignore

setup c). Skriptet importerar nödvändiga moduler. Sedan defineras filvägarna. Om det sedan redan finns en cleaned_data mapp så tas den bort av skriptet och gör en ny tom mapp.
          Sedan loopas varje mapp i raw_data igenom och delar upp namnet där det finns mellanslag. Endast den första delen behålls. Mappen kopieras sedan till cleaned_data med det nya namnet. Har kört skriptet och det funkar fint!.

setup d). Skriptet importerar nödvändiga moduler. Funktionen laddar in CSV-data till Duckdb-databas. Translation_table ersätter svenska bokstäver som å,ä och ö med a,a och o. for directory_path in CLEANED_DATA_PATH.glob("*") letar upp alla filer och mappar i CLEANED_DATA_PATH. 
          skapar sedan ett schema i databasen. Inuti varje mapp hittar skriptet varje CSV-fil. För varje fil skapas ett tabellnamn. För varje CSV-fil skapas ett schema i databasen om det inte redan finns. 
          skapas en tabell i det schemat, och data från CSV-filen laddas in i tabellen med hjälp av read_csv_auto(). Skriptet körs genom att anropa ingest_csv_data_to_duckdb() om det körs direkt.
          Har kört skripet och databasen fylldes upp.
          
setup e). EDA gjord. kan behöva återkomma hit för att justera lite olika saker.




![alt text](image.png)