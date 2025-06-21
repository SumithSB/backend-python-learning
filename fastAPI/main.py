from fastapi import FastAPI
from google.cloud import firestore
import json
import uuid
from models.category import Category


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


@app.post("/categories")
async def add_category(category: Category):
    if category.id is None:
        category.id = str(uuid.uuid4())
    db.collection('categories').document(category.id).set(category.model_dump())
    return {"status":"Success", "message":"Category added successfully", "data":category.model_dump()}

