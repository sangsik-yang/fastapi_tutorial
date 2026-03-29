import datetime
from pydantic import BaseModel, field_validator, ConfigDict
from domain.user.user_schema import User

class Comment(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    modify_date: datetime.datetime | None
    user: User | None
    answer_id: int

    model_config = ConfigDict(from_attributes=True)

class CommentCreate(BaseModel):
    content: str

    @field_validator('content')
    @classmethod
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class CommentUpdate(CommentCreate):
    comment_id: int
