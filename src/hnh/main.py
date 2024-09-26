from typing import Union
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request

import random

app = FastAPI()

html = Jinja2Templates(directory="public")

@app.get("/hello")
def read_root():
    return {"Hello": "hotdog"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = random.choice([hotdog, dog])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})


@app.get("/predict")
def hotdog():
    
    return {"Hello": random.choice(["hotdog", "not hotdog"])}

