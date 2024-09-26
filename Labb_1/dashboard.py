import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend
from frontend.kpi import DeviceKPI
from frontend.kpi import OSKPI


device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
os_kpi = OSKPI()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    st.sidebar.header("Välj alternativ tack")
    
    # initierar session state om den inte redan är det
    if "active_button" not in st.session_state:
        st.session_state.active_button = None

    
    if st.sidebar.button("Kpier för videos"):
        st.session_state.active_button = "button_1"
    if st.sidebar.button("Kpier för enheter"):
        st.session_state.active_button = "button_2"
    if st.sidebar.button("Kpier för operativsystem"):
        st.session_state.active_button = "button_3"
    if st.sidebar.button("val 4"):
        st.session_state.active_button = "button_4"

    
    if st.session_state.active_button == "button_1":
        content_kpi.display_content()
        views_graph.display_plot()
    elif st.session_state.active_button == "button_2":
        device_kpi.display_device_views()
    elif st.session_state.active_button == "button_3":
        os_kpi.display_os_uses()
    elif st.session_state.active_button == "button_4":
        st.markdown("Innehåll för val 4")
    
   
    
    
    
    
    
    
    

if __name__ == "__main__":
    layout()