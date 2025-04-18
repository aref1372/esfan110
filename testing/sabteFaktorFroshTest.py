import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.kunde import Kunde
from models.kategori import Kategori
from models.produkt import Produkt
from models.faktorF import FaktorF
from models.laga import Laga
from services.sabteFaktorFrosh import create_faktor_forosh  # فرض می‌کنیم متد در این فایل است

# تنظیمات پایگاه داده تستی
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # پایگاه داده موقتی در حافظه

# راه‌اندازی موتور پایگاه داده و جلسه
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ایجاد جدول‌ها
from models.base import Base
Base.metadata.create_all(bind=engine)

# داده‌های تست
@pytest.fixture(scope="module")
def setup_data():
    # ساخت یک جلسه از پایگاه داده
    session = SessionLocal()

    # ایجاد دسته‌بندی
    kategori = Kategori(name="Ghlamkari")
    session.add(kategori)
    session.flush()

    # ایجاد محصول
    produkt = Produkt(name="sofre", size="1*1.5", frosheOmde=500, frosheTak=700, kategori_id=kategori.id)
    session.add(produkt)
    session.flush()

    # ایجاد مشتری
    kunde = Kunde(name="Ali", nachname="Rezaei", tel="09123456789", email="ali@example.com", kundegori="T", kundenArt="Web")
    session.add(kunde)
    session.commit()

    laga = Laga(
    produkt_id=produkt.id,  # باید مطمئن شی این `produkt` همونیه که ساختی
    datum=datetime.now(),
    mojodi=5  # هرچقدر که بخوای
)
    session.add(laga)
    session.flush()

    yield session  # داده‌ها و جلسه را برای استفاده در تست‌ها برمی‌گرداند

    session.close()  # پایان جلسه


def test_create_faktor_forosh(setup_data):
    session = setup_data

    # داده‌های مورد نیاز برای فراخوانی متد
    kunde_data = {
        'name': 'Ali',
        'nachname': 'Rezaei',
        'tel': '09123456789',
        'email': 'ali@example.com',
        'kundegori': 'T',
        'kundenArt': 'Web'
    }

    produkt_name = "sofre"
    size = "1*1.5"
    kategori_name = "Ghlamkari"
    robat = 10  # تخفیف 50,000 تومان
    menge =2

    # فراخوانی متد ایجاد فاکتور فروش
    create_faktor_forosh(
        session=session,
        kunde_data=kunde_data,
        produkt_name=produkt_name,
        size=size,
        kategori_name=kategori_name,
        menge=menge,
        robat=robat
    )

    # بررسی اینکه فاکتور ایجاد شده باشد
    faktor = session.query(FaktorF).filter_by(kunde_id=1).first()
    assert faktor is not None, "Faktor Forosh sabt nashode"
    assert faktor.gesamtPreis > 0, "Gheymat kol baraye faktor sahiye nist"

    # بررسی موجودی جدید در انبار
    last_laga = session.query(Laga).order_by(Laga.id.desc()).first()
    new_mojodi = last_laga.mojodi - menge
    if new_mojodi <= 2:
            raise ValueError(f" von diese Produkt nur  {new_mojodi}  ist in der Laga ")
            assert last_laga.mojodi == 2, f" Tedade mojod dar Laga : {last_laga.mojodi} "

    print(f"Faktor sabt shod: {faktor.gesamtPreis} Euro.")

