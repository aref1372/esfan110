from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  


class Laga(Base):
    __tablename__ = 'laga'

    id = Column(Integer, primary_key=True)
    produkt_id = Column(Integer, ForeignKey('produkt.id'))
    faktorKh_id = Column(Integer, ForeignKey('faktorKh.id'))
    faktorF_id = Column(Integer, ForeignKey("faktorF.id"))
    datum = Column(Date)
    mojodi = Column(Integer)
    produkter = relationship('Produkt', back_populates='lagaha')
    faktorKher = relationship('FaktorKh', back_populates='lagaha')
    faktorFer = relationship('FaktorF' , back_populates='lagaha')
