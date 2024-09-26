from typing import Union
from fastapi import FastAPI

import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict")
def hotdog():
    return {"Hello": random.choice(["hotdog", "not hotdog"])}

