from pydantic import BaseModel, field_validator, ConfigDict


class Tag(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class TagCreate(BaseModel):
    name: str

    @field_validator("name")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Empty tag name not allowed")
        return v


class TagUpdate(BaseModel):
    id: int
    name: str


class QuestionTagAssociate(BaseModel):
    question_id: int
    tag_ids: list[int]


class QuestionTagDissociate(BaseModel):
    question_id: int
    tag_ids: list[int]


class TagDelete(BaseModel):
    tag_id: int


class TagList(BaseModel):
    total: int = 0
    tag_list: list[Tag] = []
