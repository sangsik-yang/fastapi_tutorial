import datetime

from pydantic import BaseModel, field_validator, ConfigDict
from domain.user.user_schema import User
from domain.comment.comment_schema import Comment

class AnswerCreate(BaseModel):
    content:str

    @field_validator('content')
    def not_empty(cls,v):
        if not v or not v.strip():
            raise ValueError("Empty content not allowed")
        return v

class Answer(BaseModel):
    id:int
    content:str
    create_date:datetime.datetime
    user:User | None
    question_id: int
    modify_date: datetime.datetime | None
    voter: list[User] = []
    comments: list[Comment] = []

    model_config = ConfigDict(from_attributes=True)


class AnswerUpdate(AnswerCreate):
    answer_id: int

class AnswerDelete(BaseModel):
    answer_id: int

class AnswerVote(BaseModel):
    answer_id: int
