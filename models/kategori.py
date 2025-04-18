# models/kategori.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Kategori(Base):
    __tablename__ = "kategori"
    
    id = Column(Integer, primary_key=True)
    name = Column(String , nullable=False)
    
    # فقط رابطه با محصول
    produkter = relationship("Produkt", back_populates="kategorien")
    taminKner = relationship("TaminK", back_populates="kategorien")
