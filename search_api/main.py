import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from decide_emotion.decide_emotion import EmotionDecider

df = pd.read_csv('final_tf_idf.csv', names=['word', 'tf_idf', 'emotion'], encoding='CP949')
decider = EmotionDecider(df=df)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/emotion")
async def emotion(text: str):
    return {
        "decided emotion": decider.decide(text)
    }


@app.get("/search")
async def search():

    return {}
