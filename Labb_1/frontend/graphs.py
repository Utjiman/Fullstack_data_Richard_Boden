from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)


class OSGraph:
    def __init__(self, os_data) -> None:
        self.df = os_data

    def display_os_graph(self, selected_os):
         # Filtrera data baserat på valt operativsystem
        filtered_data = self.df[self.df['Operativsystem'] == selected_os]

        visningar = filtered_data['Visningar'].values[0]
        visningstid = filtered_data['Visningstid (timmar)'].values[0]

        # Graf för visningar
        fig_visningar = px.bar(
            x=[selected_os],
            y=[visningar],
            title=f'Visningar för {selected_os}',
            labels={'x': 'Operativsystem', 'y': 'Antal Visningar'},
            color_discrete_sequence=['#636EFA']
        )

        # Graf för visningstid
        fig_visningstid = px.bar(
            x=[selected_os],
            y=[visningstid],
            title=f'Visningstid (timmar) för {selected_os}',
            labels={'x': 'Operativsystem', 'y': 'Visningstid (timmar)'}, 
            color_discrete_sequence=['#EF553B']
        )

        # Visa båda graferna bredvid varandra
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig_visningar)
        with col2:
            st.plotly_chart(fig_visningstid)

class PrenumerantsGraph:
    def __init__(self, df):
        self.df = df

    def display_prenumerants_pie_chart(self):
        # Skapar Pi-chart för visningar baserat på prenumerationsstatus
        fig = px.pie(self.df, names='Prenumerationsstatus', values='Total_Visningar', 
                     title='Fördelning av Visningar baserat på Prenumerationsstatus',
                     labels={'Prenumerationsstatus': 'Prenumerationsstatus', 'Total_Visningar': 'Antal Visningar'})
        
        
        st.plotly_chart(fig) 
        
