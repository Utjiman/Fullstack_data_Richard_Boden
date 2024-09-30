import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend
from frontend.kpi import DeviceKPI
from frontend.kpi import OSKPI
from frontend.kpi import PrenumerantsKPI
from pathlib import Path



image_path_left = Path(__file__).parent / "image/left-image.png"
image_path_right = Path(__file__).parent / "image/right-image.png"

# Skapar instanser av olika KPI-klasser
device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
os_kpi = OSKPI()
prenumerants_kpi = PrenumerantsKPI()

def layout():
    
    st.sidebar.header("Välj alternativ tack")  # Rubrik för sidomenyn

    # Skapa tre kolumner: vänster bild, KPI-sektion och höger bild
    col1, col2, col3 = st.columns([1, 9, 1])  # 1, 2, 1 fördelar utrymme: smala kolumner för bilder och bredare för KPI:er
    
    # Vänster kolumn: Visa en statisk bild
    with col1:
        st.image(str(image_path_left), use_column_width=True)
    
    # Höger kolumn: Visa en statisk bild
    with col3:
        st.image(str(image_path_right), use_column_width=True)
    
    # Mitten kolumn: Dynamiskt innehåll baserat på knapptryck
    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <h1>The Data Driven Youtuber</h1>
                <p>Den här dashboarden syftar till att utforska datan i min youtubekanal</p>
            </div>
            """, unsafe_allow_html=True)  # Centrerar rubrik och text
        # Initierar session state om det inte redan är det
        if "active_button" not in st.session_state:
            st.session_state.active_button = None

        # Knappar för att välja KPI
        if st.sidebar.button("Kpier för videos"):
            st.session_state.active_button = "button_1"
        if st.sidebar.button("Kpi för enheter"):
            st.session_state.active_button = "button_2"
        if st.sidebar.button("Kpi för operativsystem"):
            st.session_state.active_button = "button_3"
        if st.sidebar.button("Kpi för prenumeranter"):
            st.session_state.active_button = "button_4"

        # Visar dynamiskt innehåll baserat på vilken knapp som trycks
        if st.session_state.active_button == "button_1":
            content_kpi.display_content()
            views_graph.display_plot()
        elif st.session_state.active_button == "button_2":
            device_kpi.display_device_views()
        elif st.session_state.active_button == "button_3":
            os_kpi.display_os_uses()
        elif st.session_state.active_button == "button_4":
            prenumerants_kpi.display_prenumerants()


    
    
   
    
if __name__ == "__main__":
    layout()