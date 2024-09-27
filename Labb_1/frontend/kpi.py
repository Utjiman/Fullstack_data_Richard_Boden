import streamlit as st
from utils.query_database import QueryDatabase
from frontend.graphs import OSGraph
from frontend.graphs import PrenumerantsGraph

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
        
        # Räkna ut total visningar och total visningstid
        total_visningar = df['Visningar'].sum()
        total_visningstid = df['Visningstid (timmar)'].sum()

        st.markdown("## KPI för enheter och Visningstid per enhet (i timmar)")
        col1, col2 = st.columns(2)

        # Visa totala visningar och visningstid för alla enheter
        with col1:
            st.metric(label="Totala Visningar alla Enheter", value=f"{total_visningar:,}")

        with col2:
            st.metric(label="Totala Visningstid (timmar) alla Enheter", value=round(total_visningstid, 2))

        # Lägg till en dropdown-meny för att välja enhetstyp
        if 'selected_device' not in st.session_state:
            st.session_state.selected_device = df['Enhetstyp'].iloc[0]  # Standardvärde om inget är valt tidigare

        selected_device = st.selectbox('Välj enhetstyp', df['Enhetstyp'].unique(), index=df['Enhetstyp'].tolist().index(st.session_state.selected_device))

        # Spara valet i session state
        st.session_state.selected_device = selected_device

        # Filtrera data baserat på vald enhetstyp
        filtered_data = df[df['Enhetstyp'] == selected_device]

        # Hämta värden för vald enhet
        visningar = filtered_data['Visningar'].values[0]
        visningstid = filtered_data['Visningstid (timmar)'].values[0]

        # Räkna ut andelen visningar för den valda enheten
        device_share = (visningar / total_visningar) * 100

        # Visa metrics för vald enhet
        col3, col4, col5 = st.columns(3)

        with col3:
            st.metric(label="Totala Visningar", value=f"{visningar:,}")
        
        with col4:
            st.metric(label="Totala Visningstid (timmar)", value=round(visningstid, 2))
        
        with col5:
            st.metric(label="Andel Visningar från enhet", value=f"{device_share:.2f}%")

        

class OSKPI:
    def __init__(self) -> None:
        self._os = QueryDatabase("SELECT * FROM marts.cleaned_os;").df
        self.os_graph = OSGraph(self._os)  # Skapa en instans av OS-grafklassen
        
        
    def display_os_uses(self):
        df = self._os

        total_visningar = df['Visningar'].sum()
        total_visningstid = df['Visningstid (timmar)'].sum()

        st.markdown("## KPI för operativsystem och Visningstid i timmar")
        col1, col2 = st.columns(2)

        # Visa total visningar och visningstid för alla operativsystem
        with col1:
            st.metric(label="Totala Visningar alla OS", value=f"{total_visningar:,}")

        with col2:
            st.metric(label="Totala Visningstid (timmar) alla OS", value=round(total_visningstid, 2))

        # dropdown-meny för att välja operativsystem
        selected_os = st.selectbox('Välj operativsystem', df['Operativsystem'].unique())

        # Visa grafen genom att anropa grafklassen
        self.os_graph.display_os_graph(selected_os)

        # Visa den filtrerade tabellen under grafen
        filtered_data = df[df['Operativsystem'] == selected_os]
        st.dataframe(filtered_data)
        

class PrenumerantsKPI:
    def __init__(self) -> None:
        self._prenumerants = QueryDatabase("SELECT * FROM marts.cleaned_prenumerants;").df
        self.prenumerants_graph = PrenumerantsGraph(self._prenumerants) # Skapa en instans av prenumerantgrafklassen
    
    def display_prenumerants(self):
        df = self._prenumerants
        
        
        total_visningar = df['Total_Visningar'].sum()
        total_visningstid = df['Total_Visningstid'].sum()

        # Visningar från prenumeranter och icke-prenumeranter
        prenumererar_visningar = df[df['Prenumerationsstatus'] == 'Prenumererar']['Total_Visningar'].sum()
        icke_prenumererar_visningar = df[df['Prenumerationsstatus'] == 'Prenumererar inte']['Total_Visningar'].sum()

        # Beräkna andelen visningar från prenumeranter och icke-prenumeranter
        andel_prenumeranter = (prenumererar_visningar / total_visningar) * 100
        andel_icke_prenumeranter = (icke_prenumererar_visningar / total_visningar) * 100

        # Genomsnittlig visningstid per prenumerant och icke-prenumerant
        genomsnittlig_visningstid_prenumeranter = df[df['Prenumerationsstatus'] == 'Prenumererar']['Total_Visningstid'].sum() / prenumererar_visningar
        genomsnittlig_visningstid_icke_prenumeranter = df[df['Prenumerationsstatus'] == 'Prenumererar inte']['Total_Visningstid'].sum() / icke_prenumererar_visningar

        # Visa rubrik
        st.markdown("## KPI för Prenumeranter och Visningar")

        # Visa KPI (andel visningar och genomsnittlig visningstid)
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Andel Visningar från Prenumeranter", value=f"{andel_prenumeranter:.2f}%")
        with col2:
            st.metric(label="Genomsnittlig Visningstid per Prenumerant (timmar)", value=round(genomsnittlig_visningstid_prenumeranter, 2))

        # Visa KPI (andel visningar och genomsnittlig visningstid för icke-prenumeranter)
        col3, col4 = st.columns(2)
        with col3:
            st.metric(label="Andel Visningar från Icke-prenumeranter", value=f"{andel_icke_prenumeranter:.2f}%")
        with col4:
            st.metric(label="Genomsnittlig Visningstid per Icke-prenumerant (timmar)", value=round(genomsnittlig_visningstid_icke_prenumeranter, 2))

        # Visa totalt antal visningar och visningstid för alla
        col5, col6 = st.columns(2)
        with col5:
            st.metric(label="Totala Visningar", value=f"{total_visningar:,}")
        with col6:
            st.metric(label="Totala Visningstid (timmar)", value=round(total_visningstid, 2))
        

        self.prenumerants_graph.display_prenumerants_pie_chart()


        st.dataframe(df)
        
        
    
           

        
        

