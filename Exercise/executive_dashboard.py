import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Funktion för att läsa in data från CSV-filen
def read_data():
    data_path = Path(__file__).parent.parent / "Data" / "supahcoolsoftcleaned.csv" # Skapar en sökväg till CSV-filen
    df = pd.read_csv(data_path) # Läser in CSV-filen till en pandas DataFrame
    return df

def basic_statistics(df):
    total_employees = df.shape[0] # Beräknar totalt antal anställda
    average_age = df['Age'].mean() # Beräknar genomsnittsåldern
    average_salary = df['Salary_SEK'].mean() # Beräknar genomsnittslönen

    st.write(f"**Totalt antal anställda:** {total_employees}")
    st.write(f"**Genomsnittsålder:** {average_age:.2f} år")
    st.write(f"**Genomsnittslön:** {average_salary:,.2f} SEK")


def layout():
    st.set_page_config(page_title="Executive Dashboard", page_icon=":bar_chart:", layout="wide")  # Konfigurerar sidans titel och layout
    
    df = read_data()  # Läs in data

    st.title("Executive Dashboard")
    
    # Grundläggande statistik
    st.header("Grundläggande Statistik")
    basic_statistics(df)
    
    # Tabell med anställdas detaljer
    st.header("Anställdas Detaljer")
    st.dataframe(df)

    # Antal anställda per avdelning (Bar Chart med Plotly)
    st.header("Antal anställda per avdelning")
    employee_count = df['Department'].value_counts().reset_index()
    employee_count.columns = ['Department', 'Count']
    
    fig = px.bar(
        employee_count, 
        x='Department', 
        y='Count',
        title="Antal anställda per avdelning",
        labels={'Count': 'Antal anställda', 'Department': 'Avdelning'},
        width=800,  
        height=500  
    )
    
    fig.update_layout(
        xaxis_title="Avdelning",
        yaxis_title="Antal anställda",
        bargap=0.2,  
        plot_bgcolor='rgba(0,0,0,0)'  
    )
    
    st.plotly_chart(fig)

    # Histogram över lönefördelning
    st.header("Lönefördelning")
    fig = go.Figure(data=[go.Histogram(x=df['Salary_SEK'], nbinsx=10)])
    fig.update_layout(
        title_text='Lönefördelning',
        xaxis_title_text='Lön (SEK)',
        yaxis_title_text='Antal anställda',
        bargap=0.1,
        height=400,
        width=600
    )
    st.plotly_chart(fig)

    # Boxplot över löner per avdelning
    st.header("Löner per avdelning")
    fig = px.box(
        df, 
        x='Department', 
        y='Salary_SEK',
        title="Löner per avdelning",
        labels={'Department': 'Avdelning', 'Salary_SEK': 'Lön (SEK)'},
        width=800,
        height=500
    )
    
    fig.update_layout(
        xaxis_title="Avdelning",
        yaxis_title="Lön (SEK)",
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig)

    # Histogram över åldersfördelning
    st.header("Åldersfördelning")
    fig = go.Figure(data=[go.Histogram(x=df['Age'], nbinsx=10)])
    fig.update_layout(
        title_text='Åldersfördelning',
        xaxis_title_text='Ålder',
        yaxis_title_text='Antal anställda',
        bargap=0.1,
        height=400,
        width=600
    )
    st.plotly_chart(fig)

    # Boxplot över ålder per avdelning
    st.header("Ålder per avdelning")
    fig = px.box(
        df, 
        x='Department', 
        y='Age',
        title="Ålder per avdelning",
        labels={'Department': 'Avdelning', 'Age': 'Ålder'},
        width=800,
        height=500
    )
    
    fig.update_layout(
        xaxis_title="Avdelning",
        yaxis_title="Ålder",
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig)

if __name__ == "__main__":
    layout()