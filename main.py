# ==========================================================
# main.py — Chatbot Energía Viva (Gemini - Simplificado)
# ==========================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai

# Variables de entorno
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

