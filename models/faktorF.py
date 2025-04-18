from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
#from .produkt import Produkt
#from .kunde import Kunde  

class FaktorF(Base):
    __tablename__ = 'faktorF'

    id = Column(Integer, primary_key=True)
    kunde_id = Column(Integer, ForeignKey('kunde.id'), nullable=False)

    datum = Column(DateTime, nullable=False)
    robat = Column(Float)  # تخفیف
    mwstuer = Column(Float)  # مالیات
    menge = Column(Float)  # تعداد
    preis = Column(Float)  # قیمت واحد
    gesamtPreis = Column(Float)  # قیمت کل

    # روابط (اختیاری ولی مفید برای ORM)
    kundener = relationship('Kunde', back_populates='faktorFer')
    rozi110er = relationship('Rozi110' , back_populates= 'faktorFer')
    lagaha = relationship ('Laga' , back_populates='faktorFer')
    
