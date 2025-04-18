# models/kosten.py
from sqlalchemy import Column, Integer, String, Date , ForeignKey , Float
from sqlalchemy.orm import relationship
from .base import Base


class Kosten(Base):
    __tablename__ = 'kosten'

    id = Column(Integer, primary_key=True)

    mitarbeiter_id = Column(Integer, ForeignKey('mitarbeiter.id'))

    art = Column(String)  # برای 'privat' یا 'Geschäft'
    gebur = Column(Float)  # تاریخ تولد
    datum = Column(Date)  # تاریخ هزینه
    beschreibung = Column(String)  # توضیحات هزینه
    
    mitarbeiter = relationship("Mitarbeiter", back_populates="kostener")
    rozi110er = relationship('Rozi110' , back_populates= 'kostener')
