from pydantic import BaseModel
from typing import Literal


class GetMaximumRewardResponse(BaseModel):
    maximum: int


class GetAvailableRewardResponse(BaseModel):
    points: int


class PostRewardRequest(BaseModel):
    reward: str


class PostRewardSuccessResponse(BaseModel):
    success: Literal[
        "Success: Your reward points have been applied!",
        "Success: Your reward points discount has been removed!"
    ]


class PostRewardSuccessDeletionResponse(BaseModel):
    success: str = "Your reward points have been applied!"


class PostRewardErrorResponse(BaseModel):
    error: str

