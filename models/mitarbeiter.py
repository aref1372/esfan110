from sqlalchemy import Column, Integer, String
from .base import Base 
from sqlalchemy.orm import relationship

class Mitarbeiter(Base):
    __tablename__ = 'mitarbeiter'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nachname = Column(String)
    age = Column(Integer)
    tel = Column(String)
    email = Column(String)
    address = Column(String)
    
    kostener = relationship ("Kosten" ,back_populates="mitarbeiter" )
