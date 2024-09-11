import streamlit as st
import pandas as pd
from pathlib import Path
from bot import Bot

def initialize_session_state():
    """Initialize session state variables."""
    
    # Kontrollera om det finns några meddelanden i sessionen, om inte skapas en tom lista
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Kontrollera om boten är initialiserad i sessionens tillstånd, om inte skapas en ny Bot-instans
    if "bot" not in st.session_state:
        st.session_state.bot = Bot()

def display_chat_messages():
    """Display chat messages from history"""
    
    # Loopar igenom alla sparade meddelanden i sessionen och visar dem i rätt "roll" (användare eller bot)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    """Handle user input and generate bot response."""
    
    # Visar ett inmatningsfält för användaren och sparar det som 'prompt' om något skrivs in
    if prompt := st.chat_input("What is up?"):
        
        # Visar användarens inmatning i chattgränssnittet
        with st.chat_message("user"):
            st.markdown(prompt)

        # Lägger till användarens meddelande i sessionens historik
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Genererar botens svar genom att skicka användarens meddelande till Bot-klassen
        bot_response = st.session_state.bot.chat(prompt)
        response = f"Ro Båt: {bot_response}"

        # Visar botens svar i chattgränssnittet
        with st.chat_message("assistant"):
            st.markdown(response)

        # Lägger till botens svar i sessionens historik
        st.session_state.messages.append({"role": "assistant", "content": response})

def layout():
    """Define the layout of the Streamlit app."""
    st.title("Chatting with RO BÅT") # Titeln på applikationen
    st.write("RO BÅT is a funny robot that can help you out with programming tasks. However he doesn't directly answer your question, usually he asks another question back.")
    display_chat_messages() # Visar tidigare meddelanden
    handle_user_input() # Hanterar ny användarinmatning


if __name__ == "__main__":
    initialize_session_state()
    layout()