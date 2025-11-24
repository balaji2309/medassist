import os
import logging
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Gemini directly (The reliable way)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    logger.error("GOOGLE_API_KEY not found in environment!")
genai.configure(api_key=api_key)

# --- 1. Define the Server ---
app = FastAPI(title="MedAssist Agent API")

class UserQuery(BaseModel):
    text: str

# --- 2. Define the Logic ---
@app.post("/agent/query")
async def query_agent(query: UserQuery):
    """
    Directly invokes the Gemini Model for the agent response.
    """
    logger.info(f"Received query: {query.text}")
    
    try:
        # Use the specific model you confirmed works: 'gemini-flash-latest'
        model = genai.GenerativeModel('models/gemini-flash-latest')
        
        # We give the model a persona in the prompt since we are calling it directly
        system_instruction = (
            "You are MedAssist, a compassionate healthcare agent. "
            "Your goal is to help patients stay on track with their medication. "
            "If a patient misses a dose, offer safe general advice and tell them to check with their doctor. "
            "Be polite, empathetic, and concise."
        )
        
        full_prompt = f"{system_instruction}\n\nPatient: {query.text}\nMedAssist:"
        
        response = model.generate_content(full_prompt)
        return {"response": response.text}

    except Exception as e:
        logger.error(f"Agent Error: {e}")
        return {
            "response": "I'm having trouble connecting to the medical database right now.",
            "debug_error": str(e)
        }

@app.get("/")
def read_root():
    return {"message": "MedAssist Agent is Online! Visit /docs to interact."}

# --- 3. Entry Point ---
# This 'agent' variable is what Uvicorn looks for
agent = app