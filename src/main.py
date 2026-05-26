from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/store")
async def store_poster():

    return "from store"
