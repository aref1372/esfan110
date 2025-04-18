from sqlalchemy.orm import Session
from sqlalchemy import func
from models.laga import Laga
from models.produkt import Produkt


def get_mojodi_by_name_and_size(session: Session, name: str, size: str = None):
    query = session.query(
        Produkt.name.label("name"),
        Produkt.size.label("size"),
        func.sum(Laga.mojodi).label("mojodi")
    ).join(Laga, Produkt.id == Laga.produkt_id)

    # فیلتر با توجه به name و (اختیاری) size
    if name:
        query = query.filter(Produkt.name == name)
    if size:
        query = query.filter(Produkt.size == size)

    query = query.group_by(Produkt.name, Produkt.size)

    results = query.all()

    return [
        {"name": r.name, "size": r.size, "mojodi": r.mojodi}
        for r in results
    ]