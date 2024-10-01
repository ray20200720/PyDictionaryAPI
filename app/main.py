from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/words/", response_model=schemas.WordItemResponse)
def create_word_item(word: schemas.WordItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_word_item(db, word)

@app.get("/words/", response_model=List[schemas.WordItemResponse])
def read_word_items(db: Session = Depends(database.get_db)):
    return crud.get_words(db)

# @app.get("/words/{word_id}", response_model=schemas.WordItemResponse)
# def read_word_item(word_id: int, db: Session = Depends(database.get_db)):
    # db_word = crud.get_word_by_id(db, word_id)
    # if db_word is None:
        # raise HTTPException(status_code=404, detail="word item not found")
    # return db_word

@app.get("/words/{word_en}", response_model=schemas.WordItemResponse)
def read_word_item(word_en: str, db: Session = Depends(database.get_db)):
    db_word = crud.get_word_by_en(db, word_en)
    if db_word is None:
        raise HTTPException(status_code=404, detail="word item not found")
    return db_word
    
@app.put("/words/{word_id}", response_model=schemas.WordItemResponse)
def update_word_item(word_id: int, updated_word: schemas.WordItemCreate, db: Session = Depends(database.get_db)):
    db_word = crud.update_word_item(db, word_id, updated_word)
    if db_word is None:
        raise HTTPException(status_code=404, detail="word item not found")
    return db_word

@app.delete("/words/{word_id}")
def delete_word_item(word_id: int, db: Session = Depends(database.get_db)):
    db_word = crud.delete_word_item(db, word_id)
    if db_word is None:
        raise HTTPException(status_code=404, detail="word item not found")
    return {"message": "word item deleted"}