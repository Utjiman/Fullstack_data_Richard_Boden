import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# print(Path(__file__).parents[1] / "Data") # Absoluta pathen till datafoldern relativt till den här filen (03_streamlit.py).
# df = pd.read_csv("../Data/cleaned_yh_region.csv")
# print(df)

def read_data ():
    data_path = Path(__file__).parents[1] / "Data" # Definierar sökvägen till datamappen, navigerar upp en nivå från nuvarande fil och in i "Data"-mappen

    # Läser CSV-filen till en pandas DataFrame, första kolumnen används som index och tolkas som datum
    df = pd.read_csv(data_path / "cleaned_yh_region.csv", index_col=0, parse_dates=[0]) 
    
    # Ändrar indexet till att endast innehålla året (tar bort dag och månad)
    df.index = df.index.year # vill jag ha år och månad så används df.index = df.index.to_period('M'). kommer indexet att representeras som "YYYY-MM" (år och månad)
    return df

print(read_data())

def layout():
    df = read_data()
    st.markdown("# YH dashboard")
    st.markdown("Det här är en simpel dashboard om grejor")
    
    st.markdown("# Raw data")
    st.markdown("data visar grejor")
    st.dataframe(df)
    
    st.markdown("# trends per region")
    region = st.selectbox("choose region", options=df.columns)
    # st.dataframe(df[region])
    fig = px.line(data_frame=df, x= df.index, y=df[region])
    st.plotly_chart(fig)
    
    # st.markdown(region)
    
    
    
    






# __name__: Detta är en speciell variabel i Python som innehåller namnet på modulen. När en Python-fil körs direkt, 
# är värdet på __name__ satt till '__main__'. När en fil importeras som en modul i ett annat skript, 
# kommer värdet på __name__ att vara namnet på modulen (filnamnet).
# if __name__ == '__main__':: Denna sats används för att säkerställa att en viss del av koden (i detta fall anropet av layout()) 
# endast körs om skriptet körs direkt, och inte om det importeras.
if __name__ == '__main__':
    layout()
    