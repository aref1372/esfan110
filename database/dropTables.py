# database/dropTables.py
from models.base import Base, engine
from sqlalchemy import MetaData, Table
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

def drop_all_tables():
    # جمع‌آوری مدل‌ها
    models = [
        TaminK, Kategori, Produkt, AusLeihen, FaktorKh,
        FaktorF, Kosten, Kunde, Laga, Rozi110, Mitarbeiter
    ]
    
    # ایجاد متادیتا برای جدول‌ها
    meta = MetaData()
    meta.reflect(bind=engine)

    # در اینجا ترتیب حذف جداول به درستی باید رعایت شود.
    # ابتدا جدول‌هایی که به دیگران وابسته نیستند حذف می‌شوند.
    with engine.connect() as conn:
        for table in reversed(meta.sorted_tables):
            print(f"Dropping table {table.name}")
            try:
                table.drop(bind=conn, checkfirst=True)
                print("alle Tabel sind gelöscht ")
            except Exception as e:
                print(f"Error dropping table {table.name}: {e}")

if __name__ == "__main__":
    drop_all_tables()