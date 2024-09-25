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
    device_kpi.display_device_views()
    os_kpi.display_os_uses()
    
    
    content_kpi.display_content()
    views_graph.display_plot()

if __name__ == "__main__":
    layout()