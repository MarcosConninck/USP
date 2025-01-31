from pydantic import BaseModel


class Product(BaseModel):
    """
    id: int, name, description, price
    """
    id: int
    name: str
    description: str
    price: float
