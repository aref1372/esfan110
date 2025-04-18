# models/produkt.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base



class Produkt(Base):
    __tablename__ = "produkt"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    size = Column(String, nullable=False)
    ghTd = Column(Float(precision=2), nullable=True)  # فقط ۲ رقم بعد از ممیز
    frosheOmde = Column(Float(precision=2), nullable=True)  # فقط ۲ رقم بعد از ممیز
    frosheTak = Column(Float(precision=2), nullable=True)  # فقط ۲ رقم بعد از ممیز
    created_from_faktorKh = Column(Boolean, default=False) # اینجا میشه تشخیص داد محصول صرفا ثبت شده یا خرید شده و موجوده

    kategori_id = Column(Integer, ForeignKey('kategori.id'))
    kategorien = relationship("Kategori", back_populates="produkter")

    taminK_id = Column(Integer, ForeignKey('taminK.id'))
    taminKner = relationship("TaminK", back_populates="produkter")
    lagaha = relationship('Laga', back_populates='produkter')
    ausleihener = relationship('AusLeihen', back_populates='produkter')
    
    



