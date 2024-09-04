import streamlit as st
import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pathlib import Path

def read_data ():
    data_path = Path(__file__).parents[1] / "Data" # Definierar sökvägen till datamappen, navigerar upp en nivå från nuvarande fil och in i "Data"-mappen

    # Läser CSV-filen till en pandas DataFrame
    df = pd.read_csv(data_path / "IceCreamData.csv") 
    
    
    return df

def train_model(df):
    # Använd Temperature som feature och Revenue som målvariabel
    X = df[['Temperature']]  # Feature: Temperatur
    y = df['Revenue']  # Målvariabel: Intäkter

    # Dela upp data i 80% träning och 20% test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Skapa och träna en Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)


    return model # Returnerar: model: En tränad Random Forest Regressor-modell.


def layout():
    st.markdown("## Predict Ice Cream revenue based on temperature")

    df = read_data()

    model = train_model(df)

    value = st.number_input("Enter temperature in celsius", step=0.1)

    if value:
        try:
            # Konvertera input till float och göra en prediktion
            temperature = float(value)
            prediction = model.predict(np.array([[temperature]]))[0]

            # Visa prediktionen
            st.write(f"Predicted Revenue: ${prediction:.2f}")
        except ValueError:
            st.write("Please enter a valid number for the temperature.")

    

if __name__ == '__main__':
    layout()