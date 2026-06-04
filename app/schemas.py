from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class SalesTransaction(BaseModel):
    transaction_id: str = Field(..., min_length=1)
    customer_id: str = Field(..., min_length=1)
    product_id: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    unit_price: float = Field(..., gt=0)
    currency: Literal["USD", "EUR", "INR"]
    transaction_timestamp: datetime
