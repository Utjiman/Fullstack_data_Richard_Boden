# Labb 1
### setup 

#### a)
Clonade repot och kopierade in 10_lab_overview in i mitt repo.

#### b) 
Lagt till i .gitignore

#### c)
Skriptet importerar nödvändiga moduler. Sedan defineras filvägarna. Om det sedan redan finns en cleaned_data mapp så tas den bort av skriptet och gör en ny tom mapp.

Sedan loopas varje mapp i 'raw_data' igenom och delar upp namnet där det finns mellanslag. Endast den första delen behålls. Mappen kopieras sedan till 'cleaned_data' med det nya namnet. Har kört skriptet och det funkar fint!.

#### d) 
Skriptet importerar nödvändiga moduler. Funktionen laddar in CSV-data till Duckdb-databasen.

- `translation_table` ersätter svenska bokstäver som å, ä och ö med a, a och o.
- `for directory_path in CLEANED_DATA_PATH.glob("*")` letar upp alla filer och mappar i CLEANED_DATA_PATH.

Skriptet skapar ett schema i databasen, och för varje CSV-fil i mappen skapas ett tabellnamn. Data laddas in i tabellen med hjälp av `read_csv_auto()`. 

Har kört skriptet och databasen fylldes upp.
          
#### e)
EDA gjord. Tycker det är svårt att veta vad man ska göra i en EDA. Mer träning behövs! 



# uppgift 1 - plocka ut intressant data

#### a, b)
- Började med att rensa datan.
- Skapade ett skript som jag döpte till `cleaning_data.sql`, där jag gjorde några querys för att rensa data och skapa nya tabeller för användning senare.

Sedan skapade jag ett marts-schema med:
```sql
CREATE SCHEMA IF NOT EXISTS marts;
```
`cleaning_data.sql` har nu tagits bort och all rensning och justering av tabell och liknande sker nu i respektive marts.sql-fil


 
## uppgift 2 - skapa en frontend dashboard

#### a) 
Done!

#### b)
 Valde att gör kpier på enheter, os och prenumeranter som jag gjort olika visualiseringar med metrics och grafer m.m

#### c) 
Flera filtreringar är implementerade.

#### d)
 La in en meny på vänstersidan med knappar som väljer vilken kpi man vill titta på. Hittade några videos som förklarade rätt enkelt hur man gjorde. Har även grejat lite med css och lagt in två stycken bilder i kolumn 1 och 3. Kolumn 2 innehållet är baserat på vilken knapp man tryckt in, annars är den tom.



Skapat en requirements.txt fil vilket behövdes för att deploya appen på https://fullstackdatarichardboden.streamlit.app/ genom Streamlit Community Cloud.


Referenser

https://www.youtube.com/watch?v=v90luNr14Xw

https://www.youtube.com/watch?v=saOv9z6Fk88&t=408s

https://www.youtube.com/watch?v=74c3KaAXPvk

https://docs.streamlit.io/develop/api-reference/media/st.image

https://discuss.streamlit.io/t/how-to-add-images-in-the-empty-space/51269