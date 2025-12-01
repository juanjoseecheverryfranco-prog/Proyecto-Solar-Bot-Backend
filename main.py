# ==========================================================
# main.py — Chatbot Energía Viva (Gemini)
# ==========================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random

# Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Variables de entorno
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("API KEY DETECTADA:", "SÍ" if GOOGLE_API_KEY else "NO")

app = Flask(__name__)
CORS(app) # Habilitar CORS

# ==========================================================
# 🔧 Configuración de Gemini
# ==========================================================
if not GOOGLE_API_KEY:
    print("❌ ERROR: No se encontró la GOOGLE_API_KEY en el archivo .env")

# ==========================================================
# 🌐 Rutas Flask
# ==========================================================

@app.route("/")
def home():
    return "Backend de Chatbot Energía Viva Activo 🚀"

# --- CHAT ---
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_text = data.get("message", "").strip() if data else ""
    
    if not user_text:
        return jsonify({"response": "Por favor escribe algo 😅"})

    try:
        # Configuración del modelo (Usamos gemini-2.5-flash por estabilidad y velocidad)
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY)
        
        # Prompt del Sistema solicitado
        system_prompt = (
            "Eres un asistente experto. Responde preguntas respecto paneles solares, "
            "usos, beneficios, formas de instalación, enfocado para caficultores "
            "en el eje cafetero Colombiano."
        )
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_text),
        ]
        
        response = llm.invoke(messages)
        return jsonify({"response": response.content})

    except Exception as e:
        print("⚠ Error con Gemini:", e)
        return jsonify({"response": "Lo siento, tuve un problema al procesar tu solicitud. Intenta de nuevo."})


# ==========================================================
# 🚀 Ejecutar servidor
# ==========================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
