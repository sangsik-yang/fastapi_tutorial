from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.tag import tag_schema, tag_crud
from models import Question
from domain.user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix="/api/tag",
)


@router.get("/list", response_model=tag_schema.TagList)
def tag_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, tag_list = tag_crud.get_tag_list(db, skip=page * size, limit=size)
    return {"total": total, "tag_list": tag_list}


@router.get("/detail/{tag_id}", response_model=tag_schema.Tag)
def tag_detail(tag_id: int, db: Session = Depends(get_db)):
    tag = tag_crud.get_tag(db, tag_id=tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found"
        )
    return tag


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=tag_schema.Tag)
def tag_create(tag_create: tag_schema.TagCreate, db: Session = Depends(get_db)):
    return tag_crud.create_tag(db=db, tag_create=tag_create)


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def tag_update(tag_update: tag_schema.TagUpdate, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag(db=db, tag_id=tag_update.id)
    if not db_tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found"
        )
    tag_crud.update_tag(db=db, db_tag=db_tag, tag_update=tag_update)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def tag_delete(tag_delete: tag_schema.TagDelete, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag(db=db, tag_id=tag_delete.tag_id)
    if not db_tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found"
        )
    tag_crud.delete_tag(db=db, db_tag=db_tag)


@router.post("/associate", status_code=status.HTTP_204_NO_CONTENT)
def tag_associate(
    tag_assoc: tag_schema.QuestionTagAssociate, db: Session = Depends(get_db)
):
    tag_crud.associate_question_tag(
        db=db, question_id=tag_assoc.question_id, tag_ids=tag_assoc.tag_ids
    )


@router.post("/dissociate", status_code=status.HTTP_204_NO_CONTENT)
def tag_dissociate(
    tag_dis: tag_schema.QuestionTagDissociate, db: Session = Depends(get_db)
):
    tag_crud.dissociate_question_tag(
        db=db, question_id=tag_dis.question_id, tag_ids=tag_dis.tag_ids
    )


@router.get("/question/{question_id}", response_model=list[str])
def get_question_tags(question_id: int, db: Session = Depends(get_db)):
    tags = tag_crud.get_question_tags(db, question_id=question_id)
    return tags
