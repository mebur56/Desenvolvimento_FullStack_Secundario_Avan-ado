from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class DefaultResponse(BaseModel):
    message: str
    
class CategoryQuery(BaseModel):
    category: str
    year: int   

class LaureateQuery(BaseModel):
    id: int

class TranslatedText(BaseModel):
    en: Optional[str] = None
    no: Optional[str] = None
    se: Optional[str] = None
    
class LaureateParams(BaseModel):
    ids: List[int] = Field(..., description="Lista de IDs dos laureados")

class Link(BaseModel):
    rel: str
    href: str
    action: str
    types: str


class Laureate(BaseModel):
    id: str
    knownName: Dict[str, str]
    fullName: Dict[str, str]
    motivation: Dict[str, str]


class NobelPrize(BaseModel):
    awardYear: str
    category: TranslatedText
    categoryFullName: TranslatedText
    dateAwarded: str
    prizeAmount: int
    prizeAmountAdjusted: int
    laureates: List[Laureate]

class NobelResponse(BaseModel):
    nobelPrizes: List[NobelPrize]
