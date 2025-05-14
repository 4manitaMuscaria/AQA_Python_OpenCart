from pydantic import BaseModel


class AddCustomerResponse(BaseModel):
    success: str = "You have successfully modified customers"
