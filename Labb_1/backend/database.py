
import duckdb

class Database:
    """Database class with connection implemented as context manager"""

    # Konstruktor för att skapa en databasinstans och spara sökvägen till databasen
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.connection = None

    # Denna metod gör att klassen kan användas som en "context manager" med `with`-sat
    def __enter__(self):
        # Skapa en anslutning till DuckDB-databasen när `with`-satsen påbörjas
        self.connection = duckdb.connect(self.db_path)
        return self

    # Denna metod stänger anslutningen automatiskt när `with`-satsen avslutas
    def __exit__(self, exc_type, exc_value, traceback):
        # Om det finns en aktiv anslutning, stäng den
        if self.connection:
            self.connection.close()

    # Metod för att köra en SQL-fråga och returnera resultatet som en lista
    def query(self, query):
        # Använd den öppna anslutningen för att köra SQL-frågan
        return self.connection.execute(query).fetchall() # `fetchall()` returnerar alla resultat som en lista
    
# Subklass som ärver från `Database` och modifierar `query`-metoden för att returnera en pandas DataFrame
class DatabaseDataFrame(Database):
    # Modifierad `query`-metod för att returnera resultatet som en DataFrame
    def query(self, query):
        # Returnera resultaten av SQL-frågan som en pandas DataFrame
        return self.connection.execute(query).df()
