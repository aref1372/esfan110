# models/taminK.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
#from .kategori import Kategori

class TaminK(Base):
    __tablename__ = "taminK"

    # تعریف ستون‌ها
    id = Column(Integer, primary_key=True)
    firmaN = Column(String , nullable=False)
    name = Column(String)
    email = Column(String , nullable=True)
    tel = Column(String , nullable=False)
     # کلید خارجی به جدول Kategori
    kategori_id = Column(Integer, ForeignKey('kategori.id'))
    kategorien =relationship("Kategori" , back_populates="taminKner")
    
    # ارتباط ها با جداول دیگر 
    produkter= relationship("Produkt" , back_populates="taminKner")
    
    faktorKher = relationship("FaktorKh", back_populates="taminKner")
    
   

    
   
    
