from pydantic import BaseModel,Field

class products(BaseModel):
    title: str = Field(min_length=2)
    category: str = Field(min_length=2,max_length=10)
    brand: str = Field(min_length=2)
    price: float = Field(gt=500)
    stock_quantity: int = Field(default=1)
    is_available: bool = Field(default=True)
