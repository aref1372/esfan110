
# from services.sabteProduktAsFaktorkh import create_produkt_faktorkh
# from services.sabteFaktorFrosh import create_faktor_forosh
# from datetime import date
# from sqlalchemy.orm import Session
# from models.base import SessionLocal
# from models import *
# from models.base import SessionLocal

# # اینها برای متد موحودی انبار هستن 
# from services.mojodiAnbar import get_mojodi_by_name_and_size
from backend.routers import faktor
from fastapi import FastAPI
 
app = FastAPI()
app.include_router(faktor.router)

 # اگر خواستی یک روت ساده هم اضافه کن برای تست
@app.get("/")
def read_root():
    return {"message": "سلام خوش اومدی به حساب110"}


def main():

    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


    

   
    # kunde_data = {
    # 'name': 'Katia',
    # 'nachname': 'medwedewa',
    # 'tel': '0934567',
    # 'email': 'ali@exale.com',
    # 'kundegori': 'O',
    # 'kundenArt': 'Instagram'
    # }

    # with SessionLocal() as session:
    #     create_faktor_forosh(
    #         session=session,  # ✅ درست
    #         kunde_data=kunde_data,
    #         produkt_name='sofre',
    #         size='80*80',
    #         kategori_name='ghlamkari',
    #         menge=1
    # )




    # with SessionLocal() as session:
    #     create_produkt_faktorkh(
    #     session=session,
    #     kategori_name="ghlamkari",  
    #     tamink_data={
    #         "firmaN": "mahmodi",
    #         "name": " momany",  
    #         "tel": "02785625545",
    #         "email": "kontakt@mediamarkt.de"
    #     },
    #     produkt_data={
    #         "name": "sofre",
    #         "size": "1*1",  
        
    #     },
    #     faktor_data={
    #         "anzahl": 10,
    #         "ghTomn": 850000
    #     },
    #     kauf_datum=date.today()
    # )



    # اسم و سایز رو مثلاً از ورودی کاربر بگیر
    # name_input = input("sofre")
    # size_input = input("").strip()
    # size_input = size_input if size_input else None

    # session = SessionLocal()

    # try:
    #     results = get_mojodi_by_name_and_size(session, name_input, size_input)
    #     if results:
    #         for item in results:
    #             print(f"📦 {item['name']} ({item['size']}) ➤ {item['mojodi']} Muss in der Laga sein (faktorkh - faktorF)")
            
    #     else:
    #         print("❌ محصولی با این مشخصات یافت نشد.")
    # finally:
    #     session.close()


if __name__ == '__main__':
    main()

    
    





    
