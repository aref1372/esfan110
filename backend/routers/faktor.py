from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.get_db import get_db
from services.sabteProduktAsFaktorkh import create_produkt_faktorkh
from pydantic import BaseModel
from datetime import date

router = APIRouter(
    prefix="/api/faktor",
    tags=["FaktorKh"]
)

class FaktorCreate(BaseModel):
    kategori_name: str
    tamink_data: dict
    produkt_data: dict
    faktor_data: dict
    kauf_datum: date

@router.post("")
def create_faktor(faktor: FaktorCreate, db: Session = Depends(get_db)):
    create_produkt_faktorkh(
        session=db,
        kategori_name=faktor.kategori_name,
        tamink_data=faktor.tamink_data,
        produkt_data=faktor.produkt_data,
        faktor_data=faktor.faktor_data,
        kauf_datum=faktor.kauf_datum
    )
    return {"message": "Faktor created successfully"}
