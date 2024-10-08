from fastapi import FastAPI,Response
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"Home":"/"}

@app.get('/ask')
def ask(prompt :str):

    res = requests.post('http://ollama:11434/api/generate', json={
        "prompt": prompt,
        "stream" : False,
        "model" : "llama3.2:1b"
    })

    return Response(content=res.text, media_type="application/json")