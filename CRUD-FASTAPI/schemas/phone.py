from typing import Optional
from pydantic import BaseModel
class Phone(BaseModel):
    id: Optional[str]
    brand: str
    model: str
    price: str
    stock: str