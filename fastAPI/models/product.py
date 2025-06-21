from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from models.location import LocationModel

class Product(BaseModel):
    title: str
    description: Optional[str]
    seller_id: str
    category_id: str
    price: float
    condition: str
    is_sold: Optional[bool] = False
    location: LocationModel
    images: List[str]
    created_at: Optional[datetime] = None