from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.comment import comment_schema, comment_crud
from domain.answer import answer_crud
from domain.user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix="/api/comment",
)

@router.post("/create/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def comment_create(answer_id: int,
                  _comment_create: comment_schema.CommentCreate,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    answer = answer_crud.get_answer(db, answer_id=answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    comment_crud.create_comment(db, answer=answer,
                              comment_create=_comment_create,
                              user=current_user)

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def comment_update(_comment_update: comment_schema.CommentUpdate,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_comment = comment_crud.get_comment(db, comment_id=_comment_update.comment_id)
    if not db_comment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Comment not found")
    if current_user.id != db_comment.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User does not have permission to perform this action")
    comment_crud.update_comment(db=db, db_comment=db_comment,
                              comment_update=_comment_update)

@router.delete("/delete/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def comment_delete(comment_id: int,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_comment = comment_crud.get_comment(db, comment_id=comment_id)
    if not db_comment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Comment not found")
    if current_user.id != db_comment.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User does not have permission to perform this action")
    comment_crud.delete_comment(db=db, db_comment=db_comment)
