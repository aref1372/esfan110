from sqlalchemy.orm import Session
from datetime import datetime
from models.kunde import Kunde
from models.kategori import Kategori
from models.produkt import Produkt
from models.faktorF import FaktorF
from models.laga import Laga
from sqlalchemy import func


def create_faktor_forosh(
    session: Session,
    kunde_data: dict,
    produkt_name: str,
    size: str,
    kategori_name: str,
    menge: int,
    robat: float = 0.0,
    mwstuer: float = None,  # حالا None هست و بعداً 19٪ حساب می‌کنیم
):
    try:
        # 1. پیدا یا ایجاد مشتری
        kunde = session.query(Kunde).filter_by(
            name=kunde_data['name'],
            nachname=kunde_data['nachname'],
            email=kunde_data['email'],
            tel=kunde_data['tel']
        ).first()
        if not kunde:
            kunde = Kunde(
                name=kunde_data['name'],
                nachname=kunde_data['nachname'],
                tel=kunde_data['tel'],
                email=kunde_data['email'],
                kundegori=kunde_data['kundegori'],
                kundenArt=kunde_data['kundenArt']
            )
            session.add(kunde)
            session.flush()

        # 2. پیدا کردن دسته‌بندی
        kategori = session.query(Kategori).filter_by(name=kategori_name).first()
        if not kategori:
            raise ValueError(f"Kategorie '{kategori_name}' peyda nashod.")

        # 3. پیدا کردن محصول
        produkt = session.query(Produkt).filter_by(
            name=produkt_name,
            size=size,
            kategori_id=kategori.id
        ).first()
        if not produkt:
            raise ValueError(f"Produkt '{produkt_name}' ba size '{size}' va kategori '{kategori_name}' peyda nashod.")

        # 4. بررسی موجودی فعلی در Laga
        current_stock = (
        session.query(func.sum(Laga.mojodi))
        .filter(Laga.produkt_id == produkt.id)
        .scalar()
        ) or 0

        if menge > current_stock:
             raise ValueError(f"Mojodi kafi nist. Mojod: {current_stock}, Darkhast: {menge}")

        if current_stock - menge <= 2:
            print(f"⚠️ Tavajoh: faghat {current_stock - menge} az in mahsol dar anbar mand ast.")


        # 5. محاسبه قیمت پایه
        grund_preis = produkt.frosheOmde if menge > 5 else produkt.frosheTak
        if grund_preis is None:
            raise ValueError("Gheymat forosh baraye in produkt tayin nashode.")

        
        # قیمت بدون مالیات
        total_netto = round(grund_preis * menge, 2)

        # محاسبه مالیات کل
        mwstuer = round(total_netto * 0.19, 2)
        preis_mit_mwst = total_netto + mwstuer
        final_gesamt = round(preis_mit_mwst - robat, 2)

        # 8. ثبت فاکتور فروش
        faktor = FaktorF(
            kunde_id=kunde.id,
            datum=datetime.now(),
            robat=robat,
            mwstuer=mwstuer,                # کل مبلغ مالیات اینجا ذخیره میشه ✅
            menge=menge,
            preis=grund_preis,               # قیمت تکی قبل از مالیات ✅
            gesamtPreis=final_gesamt       # مبلغ نهایی که مشتری پرداخت کرده ✅
        )
        session.add(faktor)
        session.flush()

        laga = Laga(
            produkt_id=produkt.id,
            faktorF_id=faktor.id,
            faktorFer=faktor,
            datum=datetime.now(),
            mojodi=-menge
        )
        session.add(laga)

        # Commit نهایی
        session.commit()
        print(f"✅ Faktor Forosh sabt shod. Gheimat kol ba 19% mwst va robat: {final_gesamt} Euro .")

    except Exception as e:
        session.rollback()
        print(f"❌ Khata dar sabt faktor forosh: {e}")
        raise
