![Image](https://github.com/user-attachments/assets/e4526c27-e94f-47e1-9b46-559a331ac183)
Markdown# 🏥 MedAssist — Smart Medication Adherence Agent

![Status](https://img.shields.io/badge/Status-Prototype-blue)
![Track](https://img.shields.io/badge/Track-Agents_for_Good-green)
![Tech](https://img.shields.io/badge/Powered_by-Gemini_1.5_Flash-orange)

**MedAssist** is a privacy-first, multi-agent system designed to help patients adhere to medication schedules. It detects missed doses, provides empathetic medical education, and logs adherence data using Google's Agent Development Kit (ADK) and Gemini 1.5.

---

## 💡 The Problem
Medication non-adherence is a global health crisis, leading to worsening conditions and increased hospitalizations. Patients often forget doses, misunderstand side effects, or lack immediate guidance when they make a mistake (e.g., double dosing).

## 🤖 The Solution
MedAssist acts as an intelligent companion that:
1.  **Answers medical questions** using a grounded knowledge base.
2.  **Logs adherence** (Taken/Missed) into a structured memory.
3.  **Provides safety checks** for side effects and drug interactions.
4.  **Escalates** critical health complaints (like chest pain) by advising emergency care.

---

## ⚙️ Architecture

The system follows a modular Agentic Architecture:

```mermaid
flowchart LR
    User[Patient] <--> Frontend[Streamlit UI]
    Frontend <--> Backend[FastAPI Server]
    Backend <--> Agent[MedAssist ADK Agent]
    
    subgraph "Agent Logic (Gemini 1.5)"
        Agent -- Query --> Tools
        Tools --> DrugInfo[Drug Database]
        Tools --> Logger[Adherence Memory]
    end
Tech StackLLM: Google Gemini 1.5 Flash (via google-generativeai)Agent Framework: Google ADK (Agent Development Kit) conceptBackend: FastAPI (Python)Frontend: StreamlitDeployment: Docker / Google Cloud Vertex AI (Ready)🚀 Quick Start (Local)PrerequisitesPython 3.9+A Google Cloud API Key (AI Studio)1. Clone the RepositoryBashgit clone [https://github.com/balaji2309/medassist.git](https://github.com/balaji2309/medassist.git)
cd medassist
2. Set up EnvironmentCreate a .env file in the root directory:PlaintextGOOGLE_API_KEY=your_actual_api_key_here
3. Install DependenciesBashpython -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
pip install streamlit
4. Run the SystemYou need to run the Backend and Frontend in separate terminals.Terminal 1 (Backend):Bashuvicorn medassist_agent.agent:agent --host 0.0.0.0 --port 8000
Terminal 2 (Frontend):Bashstreamlit run frontend/app.py
Visit http://localhost:8501 to interact with the agent!🧪 Demo ScenariosTry these prompts to see the agent's capabilities:ScenarioUser PromptExpected Agent BehaviorMissed Dose"I missed my morning dose of Lisinopril. What should I do?"Offers safe advice (do not double dose) and empathy.Side Effects"I feel dizzy after taking my pills."Checks drug info tool, identifies dizziness as a side effect, advises caution.Adherence Log"I just took my Metformin."Logs the action as 'TAKEN' and confirms.Emergency"My chest hurts and I can't breathe."Safety Rail: Immediately advises calling emergency services.📂 Project StructurePlaintextmedassist/
├── medassist_agent/      # Core Agent Logic
│   └── agent.py          # FastAPI + Gemini Integration
├── frontend/             # User Interface
│   └── app.py            # Streamlit Chat App
├── agent/                # Standalone simulation scripts
├── deploy/               # Deployment documentation
├── tests/                # Unit tests
├── Dockerfile            # Container configuration
└── requirements.txt      # Python dependencies
📜 LicenseThis project is open-source under the MIT License.
