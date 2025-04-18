
# models/kunde.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base




class Kunde(Base):
    __tablename__ = 'kunde'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nachname = Column(String ,nullable=False)
    tel = Column(String, nullable=False)
    email = Column(String , nullable=False)

    # kundegori: 'T' یا 'O'
    kundegori = Column(String(1), nullable=False)

    # von wo hat kunde uns erfunden welche web oder peresens
    kundenArt = Column(String, nullable=False)

    
    faktorFer = relationship("FaktorF", back_populates="kundener")
    ausleihener = relationship("AusLeihen", back_populates="kundener")  








