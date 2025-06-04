from pydantic import BaseModel

from typing import Optional, List


class CustomField(BaseModel):
    name: str
    value: str


class AddCustomerRequest(BaseModel):
    customer_id: Optional[str] = None
    customer_group_id: str
    firstname: str
    lastname: str
    telephone: Optional[str] = None
    email: str
    custom_field: Optional[List[CustomField]] = []


class AddCustomerResponse(BaseModel):
    success: str = "You have successfully modified customers"
