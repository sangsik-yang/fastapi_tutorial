import datetime

from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer
from domain.user.user_schema import User


class Tag(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
    user: User | None
    modify_date: datetime.datetime | None
    voter: list[User] = []
    tags: list[Tag] = []

    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    subject: str
    content: str
    tag_ids: list[int] = []

    @field_validator("subject", "content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Empty content not allowed")
        return v


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []


class QuestionUpdate(QuestionCreate):
    question_id: int
    tag_ids: list[int] = []


class QuestionDelete(BaseModel):
    question_id: int


class QuestionVote(BaseModel):
    question_id: int
