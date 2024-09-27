import streamlit as st
from utils.query_database import QueryDatabase
from frontend.graphs import OSGraph

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)

class DeviceKPI:
    def __init__(self) -> None:
        self._device = QueryDatabase("SELECT * FROM marts.visningar_per_enhetstyp;").df

    def display_device_views(self):
        df = self._device
        
        total_visningar = df['Visningar'].sum()
        total_visningstid = df['Visningstid (timmar)'].sum()

        st.markdown("## KPI för enheter och Visningstid för per enhet i timmar")
        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="Totala Visningar alla Enheter", value=f"{total_visningar:,}")

        with col2:
            st.metric(label="Totala Visningstid (timmar) alla Enheter", value=round(total_visningstid, 2))
        
        # Lägg till en dropdown-meny och spara valet i session state
        if 'selected_device' not in st.session_state:
            st.session_state.selected_device = df['Enhetstyp'].iloc[0]  # Standardvärde

        selected_device = st.selectbox('Välj enhetstyp', df['Enhetstyp'].unique(), index=df['Enhetstyp'].tolist().index(st.session_state.selected_device))

        # Spara valet i session state
        st.session_state.selected_device = selected_device

        # Filtrera data baserat på vald enhetstyp
        filtered_data = df[df['Enhetstyp'] == selected_device]

        # Visa metrics för vald enhetstyp
        visningar = filtered_data['Visningar'].values[0]
        visningstid = filtered_data['Visningstid (timmar)'].values[0]

        # Visa metrics som totalsiffror
        st.metric(label="Totala Visningar", value=visningar)
        st.metric(label="Totala Visningstid (timmar)", value=round(visningstid, 2))

class OSKPI:
    def __init__(self) -> None:
        self._os = QueryDatabase("SELECT * FROM marts.cleaned_os;").df
        self.os_graph = OSGraph(self._os)  # Skapa en instans av grafklassen
        
        
    def display_os_uses(self):
        df = self._os

        total_visningar = df['Visningar'].sum()
        total_visningstid = df['Visningstid (timmar)'].sum()

        st.markdown("## KPI för operativsystem och Visningstid i timmar")
        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="Totala Visningar alla OS", value=f"{total_visningar:,}")

        with col2:
            st.metric(label="Totala Visningstid (timmar) alla OS", value=round(total_visningstid, 2))

        # Lägg till en dropdown-meny för att välja operativsystem
        selected_os = st.selectbox('Välj operativsystem', df['Operativsystem'].unique())

        # Visa grafen genom att anropa grafklassen
        self.os_graph.display_os_graph(selected_os)

        # Visa den filtrerade tabellen under grafen
        filtered_data = df[df['Operativsystem'] == selected_os]
        st.dataframe(filtered_data)
        
class PrenumerantsKPI:
    def __init__(self) -> None:
        self._prenumerants = QueryDatabase("SELECT * FROM marts.cleaned_prenumerants;").df
        
    def display_prenumerants(self):
        df = self._prenumerants
        
        
        total_visningar = df['Total_Visningar'].sum()
        total_visningstid = df['Total_Visningstid'].sum()

        st.markdown("## KPI för Prenumeranter och Visningar")
        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="Totala Visningar", value=f"{total_visningar:,}")

        with col2:
            st.metric(label="Totala Visningstid (timmar)", value=round(total_visningstid, 2))

        
        st.dataframe(df)
        
        
    
           

        
        

