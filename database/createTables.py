# database/create_tables.py
from models.base import Base, engine
from models.taminK import TaminK
from models.kategori import Kategori
from models.produkt import Produkt
from models.ausleihen import AusLeihen
from models.faktorKh import FaktorKh
from models.faktorF import FaktorF
from models.kosten import Kosten
from models.kunde import Kunde
from models.laga import Laga
from models.rosi110 import Rozi110
from models.mitarbeiter import Mitarbeiter

def create_all_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_all_tables()
