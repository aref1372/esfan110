from sqlalchemy.orm import Session
#from models.base import SessionLocal
from datetime import date
from models.kategori import Kategori
from models.taminK import TaminK
from models.produkt import Produkt
from models.faktorKh import FaktorKh
from models.laga import Laga
from sqlalchemy.exc import IntegrityError


def create_produkt_faktorkh(
    session: Session,
    kategori_name: dict,
    tamink_data: dict,
    produkt_data: dict,
    faktor_data: dict,
    kauf_datum: date
):
    try:
        # 1. پیدا یا ایجاد Kategori
        kategori = session.query(Kategori).filter_by(name=kategori_name).first()
        if not kategori:
            kategori = Kategori(name=kategori_name)
            session.add(kategori)
            session.flush()

        # 2. پیدا یا ایجاد تامین‌کننده
        tamink = session.query(TaminK).filter_by(tel=tamink_data['tel']).first()
        if not tamink:
            tamink = TaminK(
                firmaN=tamink_data['firmaN'],
                name=tamink_data.get('name'),
                email=tamink_data.get('email'),
                tel=tamink_data['tel'],
                kategorien=kategori
            )
            session.add(tamink)
            session.flush()

        # 3. پیدا یا ایجاد محصول
        produkt = session.query(Produkt).filter_by(
            name=produkt_data['name'],
            size=produkt_data['size'],
            kategori_id=kategori.id,
            taminK_id=tamink.id
        ).first()

        if not produkt:
            produkt = Produkt(
                name=produkt_data['name'],
                size=produkt_data['size'],
                ghTd=produkt_data.get('ghTd'),
                frosheOmde=produkt_data.get('frosheOmde'),
                frosheTak=produkt_data.get('frosheTak'),
                created_from_faktorKh=True,
                kategorien=kategori,
                taminKner=tamink
            )
            session.add(produkt)
            session.flush()

        # 4. فاکتور خرید
        faktor = FaktorKh(
            taminKner=tamink,
            datum=kauf_datum,
            anzahl=faktor_data['anzahl'],
            ghTomn=faktor_data['ghTomn']
        )
        session.add(faktor)
        session.flush()

        # محاسبه قیمت‌ها از ghTomn
        ghTomn = faktor_data['ghTomn']
        ghTd = round(ghTomn / 28000, 2)
        frosheTak = round(ghTd * 1.40, 2)
        frosheOmde = round(ghTd * 1.20, 2)

        if not produkt:
            produkt = Produkt(
                name=produkt_data['name'],
                size=produkt_data['size'],
                ghTd=ghTd,
                frosheTak=frosheTak,
                frosheOmde=frosheOmde,
                created_from_faktorKh=True,
                kategorien=kategori,
                taminKner=tamink
             )
            session.add(produkt)
            session.flush()
        else:
            produkt.ghTd = ghTd
            produkt.frosheTak = frosheTak
            produkt.frosheOmde = frosheOmde

        # 5. محاسبه موجودی قبلی از Laga
        last_laga = (
            session.query(Laga)
            .filter_by(produkt_id=produkt.id)
            .order_by(Laga.id.desc())
            .first()
        )
        old_mojodi = last_laga.mojodi if last_laga else 0
        # new_mojodi = old_mojodi + faktor_data['anzahl']

        new_mojodi = faktor_data['anzahl']

        # ثبت در Laga با موجودی جدید
        laga = Laga(
            produkter=produkt,
            faktorKher=faktor,
            datum=kauf_datum,
            mojodi=new_mojodi
        )
        session.add(laga)

        session.commit()
        print("✅ FaktorKhrid ba movafaghiat sabt shod .")

    except Exception as e:
        session.rollback()
        print("❌ khata da sabt", e)
        raise


    