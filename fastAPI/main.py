from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import firestore
import json

app = FastAPI()

db = firestore.Client.from_service_account_json('firebase_service_connect.json')


@app.get("/categories")
async def get_categories():
    categories_ref = db.collection('categories')
    categories = categories_ref.get()
    result = []
    for category in categories:
        result.append(category.to_dict())
    return result