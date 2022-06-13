import pandas as pd
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from decide_emotion.decide_emotion import EmotionDecider
from recommender import recommende

df = pd.read_csv('final_tf_idf.csv', names=['word', 'tf_idf', 'emotion'], encoding='CP949')
decider = EmotionDecider(df=df)

genres = ['Romance', 'Crime', 'Adventure', 'Action', 'Comedy', 'Family', 'Drama', 'Musical', 'Thriller',
          'Mystery', 'Family']


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://imsdb-search.fly.dev/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("serving start")


@app.get("/emotion")
async def emotion_route(text: str):
    return {
        "decided emotion": decider.decide(text)
    }

@app.get("/search")
async def search_route(text: str, count: int = 10):
    emotion = decider.decide(text)
    movies, genre = recommende(text=text, emotion=emotion, count=count)
    return {
        "emotion": emotion,
        "genre": genre,
        "movies": movies,
    }
