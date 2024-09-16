import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()



EDEN_API_KEY = os.getenv("EDEN_API")
class Bot:

    def __init__(self) -> None:
        self._history = [] # Lista för att hålla historiken av meddelanden mellan användaren och boten

    def chat(self, prompt):
        
        # Skapar headers för API-begäran, inklusive en API-nyckel för autentisering
        headers = {"Authorization": f"Bearer {EDEN_API_KEY}"}

        # URL för API-endpoint som hanterar chat-funktionen
        url = "https://api.edenai.run/v2/text/chat"
        
        # Skapar payload som ska skickas till API:t
        payload = {
            "providers": "openai/gpt-4o",   # Specifierar GPT-4o som leverantör av språkmodellen
            "text": prompt,                 # Skickar användarens prompt (det de har skrivit)
            
            # Definierar botens persona och instruktioner
            "chatbot_global_action": """
            You are Glenn from Göteborg, and you always speak in a Göteborg dialect. You are very passionate about Blåvitt and often make light-hearted jokes about people from Stockholm. Use phrases like "la", "gött mos", and "spårvagn" often. Always end your conversations with a Göteborgish slang. 
            """,
            # Inkluderar tidigare historik av konversationer så att boten kan hålla tråden i dialogen
            "previous_history": self._history,
            "temperature": 0.5, # Temperatur för att styra graden av kreativitet i svaren (0.5 ger en balans mellan kreativitet och precision)
            "max_tokens": 500,  # Max antal tokens (ord eller delar av ord) som modellen kan generera
        }

        # Skickar en POST-begäran till API:t med payload och headers
        response = requests.post(url, json=payload, headers=headers)

        # Extraherar det genererade svaret från API:s svar
        answer = json.loads(response.text)['openai/gpt-4o']['generated_text']

        # Lägger till användarens inmatning och botens svar i historiken. skapar minnet
        self._history.append({"role": "user", "message": prompt})
        self._history.append({"role": "assistant", "message": answer})

        # Returnerar botens svar för att visas i chatten
        return answer

