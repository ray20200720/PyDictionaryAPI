from pydantic import BaseModel

class WordItemBase(BaseModel):
    id: int 
    en: str
    part_of_speech: str
    ch: str = None

class WordItemCreate(WordItemBase):
    pass

class WordItemResponse(WordItemBase):
    id: int

    class Config:
        #orm_mode = True
        from_attributes = True
