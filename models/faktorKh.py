# models/faktorKh.py
from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base


class FaktorKh(Base):
    __tablename__ = 'faktorKh'

    id = Column(Integer, primary_key=True)
    tamink_id = Column(Integer, ForeignKey('taminK.id'))
    datum = Column(Date)
    anzahl = Column(Integer, nullable=False)  # تعداد
    ghTomn = Column(Float(), nullable=False)  # قیمت خرید به تومان
    taminKner = relationship("TaminK", back_populates="faktorKher")
    lagaha = relationship('Laga', back_populates='faktorKher')
    rozi110er = relationship('Rozi110' , back_populates= 'faktorKher')

