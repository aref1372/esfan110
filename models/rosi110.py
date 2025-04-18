# models/rozi110.py
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base
#from .faktorF import FaktorF  
#from .faktorKh import FaktorKh 
#from .kosten import Kosten
class Rozi110(Base):
    __tablename__ = 'rozi110'

    id = Column(Integer, primary_key=True)
    betrag = Column(Float)  # مبلغ سود
    beschreibung = Column(String)  # توضیحات سود
    datum = Column(Date)  # تاریخ سود
    faktorF_id = Column(Integer, ForeignKey('faktorF.id'))  # کلید خارجی به FaktorF
    faktorKh_id = Column(Integer, ForeignKey('faktorKh.id'))  # کلید خارجی به FaktorKh
    kosten_id = Column(Integer, ForeignKey('kosten.id'))
    ausleihen_id = Column(Integer, ForeignKey('ausleihen.id'))

     # Aggregated values
    total_sales = Column(DECIMAL, default=0)         # مجموع فروش‌ها
    total_purchases = Column(DECIMAL, default=0)     # مجموع خریدها
    total_loans = Column(DECIMAL, default=0)         # مجموع امانت‌ها
    total_costs = Column(DECIMAL, default=0)         # مجموع هزینه‌ها

    net_profit = Column(DECIMAL, default=0)          # سود خالص

    # روابط با جداول FaktorF و FaktorKh
    faktorFer = relationship('FaktorF', back_populates='rozi110er')
    faktorKher = relationship('FaktorKh', back_populates='rozi110er')
    kostener = relationship('Kosten', back_populates='rozi110er')
    ausleihener = relationship("AusLeihen", backref="rozi110er")
