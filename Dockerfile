FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
# Points to medassist_agent/agent.py -> variable 'agent'
CMD ["uvicorn", "medassist_agent.agent:agent", "--host", "0.0.0.0", "--port", "8000"]