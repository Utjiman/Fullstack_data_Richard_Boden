import streamlit as st
import pandas as pd 
import numpy as np
from pathlib import Path
import plotly.express as px

def read_data ():
    data_path = Path(__file__).parents[1] / "Data" # Definierar sökvägen till datamappen, navigerar upp en nivå från nuvarande fil och in i "Data"-mappen

    # Läser CSV-filen till en pandas DataFrame
    df = pd.read_csv(data_path / "OECD_PISA_data.csv")
    df['TIME'] = df['TIME'].astype(int)
    
    return df

def basic_statistics(df):
    number_of_records = len(df.index) # Räkna totalt antal poster (rader) i DataFrame
    number_of_locations = df["LOCATION"].nunique() # Räkna antal unika platser (LOCATION) utan dubbletter
    number_of_subjects = df["SUBJECT"].value_counts()  # Räkna hur många poster det finns för varje ämne (SUBJECT: BOY, GIRL, TOTAL)
    time_periods_min = df["TIME"].min()
    time_periods_max = df["TIME"].max()
    time_period = f"{time_periods_min}–{time_periods_max}" # Skapa en sträng för att visa tidsperioden (ex: 2000–2015)
    
    st.write(f"**Total number of records:** {number_of_records}")
    st.write(f"**Total number of locations no dublicates:** {number_of_locations}")
    st.write(f"**Time period:** {time_period}")
    
    st.write(f"**Number of records by subject (BOY, GIRL, TOTAL):**")
    for subject, count in number_of_subjects.items():
        st.write(f"{subject}: {count}")
    
   

def layout():
    
    # Läs in data från CSV-filen
    df = read_data()
    
    # Visa rubrik för grundläggande statistik
    st.header("Basic Statistic")
    basic_statistics(df)
    
    st.header("Sample data")
    
    # Formatera TIME-kolumnen utan kommatecken och visa den 
    df_styled = df.style.format({"TIME": "{:.0f}"})
    st.dataframe(df_styled)
    
    st.header("Avarage PISA scores by location")
    # Beräkna genomsnittliga PISA-resultat för varje plats (LOCATION)
    avarage_score = df.groupby("LOCATION")["Value"].mean().reset_index()
    
    # Skapa ett stapeldiagram med Plotly Express för att visa genomsnittliga poäng
    fig = px.bar(avarage_score,
                 x='LOCATION',
                 y='Value',
                 title="Average Score by Location",
                 labels={'Value':'Average Score'})
    
    st.plotly_chart(fig)
    
    selected_country = st.selectbox('Välj land', df['LOCATION'].sort_values(ascending=True).unique())
    filtered_data = df[df['LOCATION'] == selected_country]
    trends = filtered_data.groupby('TIME')['Value'].mean().reset_index()
    
    fig = px.line(trends, x='TIME', y='Value', title=f'Trend for {selected_country}')

    st.plotly_chart(fig)
    
if __name__ == "__main__":
    layout()
