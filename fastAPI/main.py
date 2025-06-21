from typing import List
from fastapi import FastAPI
from google.cloud import firestore
import json
import uuid
from models.product import Product
from models.category import Category


app = FastAPI()
db = firestore.Client.from_service_account_json('firebase_service_connect.json')


@app.get("/categories",response_model=List[Category])
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



@app.get("/products", response_model=List[Product])
async def get_all_products():
    products_ref = db.collection("products")
    docs = products_ref.stream()

    result = []
    for doc in docs:
        data = doc.to_dict()
        location = data.get("location")

        # Only include products with valid GeoPoint
        if not location:
            continue

        product = {
            "id": doc.id,
            "title": data.get("title"),
            "price": data.get("price"),
            "description": data.get("description"),
            "images": data.get("images", []),
            "seller_id": data.get("seller_id"),
            "category_id": data.get("category_id"),
            "condition": data.get("condition"),
            "is_sold": data.get("is_sold", False),
            "location": {
                "latitude": location.latitude,
                "longitude": location.longitude
            }
        }

        result.append(product)

    return result
