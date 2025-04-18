# models/ausleihen.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

#from .produkt import Produkt

class AusLeihen(Base):
    __tablename__ = 'ausleihen'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nachname = Column(String)
    produkt_id = Column(Integer, ForeignKey('produkt.id'))
    produkter = relationship("Produkt",back_populates= "ausleihener")
    kunden_id = Column(Integer, ForeignKey('kunde.id'))
    kundener = relationship ("Kunde" , back_populates="ausleihener")
    datum = Column(Date)
    firmaName = Column(String)
    address = Column(String)
    tel = Column(String)
    email = Column(String)
    steuernumer = Column(String)

    
   
