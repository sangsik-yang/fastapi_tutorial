from datetime import datetime

from models import Question, Tag
from sqlalchemy.orm import Session
from domain.tag.tag_schema import TagCreate, TagUpdate


def get_tag_list(db: Session, skip: int = 0, limit: int = 10):
    tag_list = db.query(Tag)
    total = tag_list.count()
    tag_list = tag_list.offset(skip).limit(limit).all()
    return total, tag_list


def get_tag(db: Session, tag_id: int):
    tag = db.query(Tag).get(tag_id)
    return tag


def create_tag(db: Session, tag_create: TagCreate):
    db_tag = Tag()
    db_tag.name = tag_create.name
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def update_tag(db: Session, db_tag: Tag, tag_update: TagUpdate):
    db_tag.name = tag_update.name
    db.add(db_tag)
    db.commit()


def delete_tag(db: Session, db_tag: Tag):
    db.delete(db_tag)
    db.commit()


def associate_question_tag(db: Session, question_id: int, tag_ids: list[int]):
    """Associate tags with a question"""
    if not question_id:
        return

    question = db.query(Question).get(question_id)
    if not question:
        return

    existing_tags = set(tag.id for tag in question.tags)

    for tag_id in tag_ids:
        tag = db.query(Tag).get(tag_id)
        if tag and tag_id not in existing_tags:
            question.tags.append(tag)


def dissociate_question_tag(db: Session, question_id: int, tag_ids: list[int]):
    """Dissociate tags from a question"""
    if not question_id:
        return

    question = db.query(Question).get(question_id)
    if not question:
        return

    for tag_id in tag_ids:
        tag = db.query(Tag).get(tag_id)
        if tag and tag in question.tags:
            question.tags.remove(tag)


def get_question_tags(db: Session, question_id: int):
    """Get all tags for a question"""
    question = db.query(Question).get(question_id)
    return [tag.name for tag in question.tags] if question else []
