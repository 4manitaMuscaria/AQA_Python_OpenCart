from pydantic import BaseModel


class AddVoucherRequest(BaseModel):
    from_name: str
    from_email: str
    to_name: str
    to_email: str
    voucher_theme_id: int
    message: str
    amount: float


class AddVoucherResponse(BaseModel):
    success: str = "Success: You have modified your shopping cart!"
