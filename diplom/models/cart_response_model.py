from typing import List
from pydantic import BaseModel, field_validator


class Voucher(BaseModel):
    key: int
    description: str
    amount: str

    @field_validator('amount')
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
