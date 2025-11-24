import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def run_simulation():
    print("--- 🏥 Starting MedAssist Simulation ---")
    patient_query = "I just took my lisinopril, but I feel dizzy. Is that normal?"
    print(f"\n👤 Patient: {patient_query}")
    
    print("\n🤖 Agent (Thinking)...")
    time.sleep(1.0)
    print("   > Identifying drug: 'lisinopril'")
    print("   > Checking database for side effects...")
    model = genai.GenerativeModel('models/gemini-flash-latest')
    prompt = f"""
    You are a medical assistant. Patient says: "{patient_query}".
    Known side effects of Lisinopril: Dizziness, dry cough.
    Log that they took the medication.
    Provide a short, empathetic response.
    """
    response = model.generate_content(prompt)
    
    print(f"\n🤖 MedAssist: {response.text}")
    print("\n[System Log] Adherence Status: TAKEN recorded.")

if __name__ == "__main__":
    run_simulation()