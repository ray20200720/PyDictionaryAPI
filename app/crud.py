from sqlalchemy.orm import Session
from . import models, schemas

def get_words(db: Session):
    return db.query(models.WordItem).all()

def get_word_by_id(db: Session, word_id: int):
    return db.query(models.WordItem).filter(models.WordItem.id == word_id).first()

def get_word_by_en(db: Session, word_en: str):
    return db.query(models.WordItem).filter(models.WordItem.en == word_en).first()
    
def create_word_item(db: Session, word: schemas.WordItemCreate):
    db_word = models.WordItem(**word.dict())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word

def update_word_item(db: Session, word_id: int, updated_word: schemas.WordItemCreate):
    db_word = db.query(models.WordItem).filter(models.WordItem.id == word_id).first()
    if db_word:
        for key, value in updated_word.dict().items():
            setattr(db_word, key, value)
        db.commit()
        db.refresh(db_word)
    return db_word

def delete_word_item(db: Session, word_id: int):
    db_word = db.query(models.WordItem).filter(models.WordItem.id == word_id).first()
    if db_word:
        db.delete(db_word)
        db.commit()
    return db_word