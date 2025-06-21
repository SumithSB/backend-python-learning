from decimal import Decimal
from pydantic import Field, BaseModel

class LocationModel(BaseModel):
    latitude: Decimal = Field(..., ge=-90, le=90)
    longitude: Decimal = Field(..., ge=-180, le=180)