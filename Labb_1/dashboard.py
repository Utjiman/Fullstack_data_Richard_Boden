import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend
from frontend.kpi import DeviceKPI
from frontend.kpi import OSKPI
from frontend.kpi import PrenumerantsKPI


device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
os_kpi = OSKPI()
prenumerants_kpi = PrenumerantsKPI()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    st.sidebar.header("Välj alternativ tack")
    
    # initierar session state om den inte redan är det
    if "active_button" not in st.session_state:
        st.session_state.active_button = None

    # Knappinteraktioner
    if st.sidebar.button("Kpier för videos"):
        st.session_state.active_button = "button_1"
    if st.sidebar.button("Kpi för enheter"):
        st.session_state.active_button = "button_2"
    if st.sidebar.button("Kpi för operativsystem"):
        st.session_state.active_button = "button_3"
    if st.sidebar.button("Kpi för prenumeranter"):
        st.session_state.active_button = "button_4"

    
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