from fastapi import FastAPI
from pydantic import BaseModel
from agents import Agent, helpful_assistant


app = FastAPI()

class AgentRequest(BaseModel):
    agent_id: str
    message: str

agents = {}

@app.post("/agent")
async def chat(request: AgentRequest):
    agent_id = request.agent_id
    if agent_id not in agents:
        agents[agent_id] = Agent.clone(helpful_assistant)
    agent = agents[agent_id]
    return agent.message(request.message)