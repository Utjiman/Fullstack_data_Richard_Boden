import streamlit as st
import pandas as pd 
import numpy as np
from pathlib import Path

def read_data ():
    data_path = Path(__file__).parents[1] / "Data" # Definierar sökvägen till datamappen, navigerar upp en nivå från nuvarande fil och in i "Data"-mappen

    # Läser CSV-filen till en pandas DataFrame
    df = pd.read_csv(data_path / "OECD_PISA_data.csv") 
    
    
    return df

print(read_data())