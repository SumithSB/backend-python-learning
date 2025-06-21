from pydantic import BaseModel


class Category(BaseModel):
    id: str | None = None
    image:str
    name:str
    parent_id:str | None = None