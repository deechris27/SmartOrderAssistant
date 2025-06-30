from db import SessionLocal, Product

db = SessionLocal()
products = db.query(Product).all()
for p in products:
    print(f"{p.id}: {p.name} - {p.category} - ${p.price} - Stock: {p.stock}")
db.close()
