from fastapi import FastAPI
from .assistant import DeepSeekAssistant

app = FastAPI()
assistants = {}

@app.post("/chat/{user_id}")
async def chat(user_id: str, message: str):
    if user_id not in assistants:
        assistants[user_id] = DeepSeekAssistant(user_id)
    return {"response": assistants[user_id].chat(message)}

@app.post("/memory/{user_id}")
async def save_memory(user_id: str):
    if user_id in assistants:
        assistants[user_id]._save_memory()
    return {"status": "Memory saved"}
    
    from fastapi import FastAPI
from .assistant import DeepSeekAssistant

app = FastAPI()
assistants = {}

@app.post("/chat/{user_id}")
async def chat(user_id: str, message: str):
    if user_id not in assistants:
        assistants[user_id] = DeepSeekAssistant(user_id)
    return {"response": assistants[user_id].chat(message)}

@app.post("/memory/{user_id}")
async def save_memory(user_id: str):
    if user_id in assistants:
        assistants[user_id]._save_memory()
    return {"status": "Memory saved"}