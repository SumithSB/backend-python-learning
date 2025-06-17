from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name:str
    age:int


@app.get("/path")
async def root(name:str):
    return {"message": f"Hello {name}"}

@app.post("/path")
async def root(item:Item):
    return {"message": item.model_dump()}


@app.post("/path/new")
async def root(item:Item):
    return {"message": item.model_dump()}