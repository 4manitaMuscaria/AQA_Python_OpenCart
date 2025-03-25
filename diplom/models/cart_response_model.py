from typing import List, Optional
from pydantic import BaseModel, validator


class Voucher(BaseModel):
    key: int
    description: str
    amount: str

    @validator('amount')
    def validate_amount(cls, value):
        if not value.startswith('$') or not value[1:].replace('.', '', 1).isdigit():
            raise ValueError("Invalid amount format")
        return float(value[1:])


class Total(BaseModel):
    title: str
    text: str


class CartResponse(BaseModel):
    products: List[dict]
    vouchers: List[Voucher]
    totals: List[Total]
    shipping_required: bool
