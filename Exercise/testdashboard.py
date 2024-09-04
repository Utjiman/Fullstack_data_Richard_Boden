import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sätt en titel och beskrivning
st.title("Min första Streamlit Dashboard")
st.write("Detta är en enkel Streamlit-app för att visualisera data.")

# Skapa en slider för att interagera med användaren
antal = st.slider("Välj antal datapunkter", min_value=10, max_value=100, value=50)

# Generera slumpmässiga data
data = np.random.randn(antal, 2)

# Visa data i en tabell
df = pd.DataFrame(data, columns=["X", "Y"])
st.write("Data som visas i tabellformat:")
st.dataframe(df)

# Visualisera data i ett scatterplot
st.write("Scatterplot av datan:")
fig, ax = plt.subplots()
ax.scatter(df['X'], df['Y'])
st.pyplot(fig)

# Skapa en checkbox för ytterligare interaktivitet
if st.checkbox("Visa datastatistik"):
    st.write(df.describe())
