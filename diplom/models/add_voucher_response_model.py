from pydantic import BaseModel


class AddVoucherResponse(BaseModel):
    success: str = "Success: You have modified your shopping cart!"
