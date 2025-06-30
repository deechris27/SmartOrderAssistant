from db import SessionLocal, Product

db = SessionLocal()

products = [
    Product(name="Syringe 5ml", category="Medical", sku="MED123", price=2.5, stock=500),
    Product(name="Syringe 10ml", category="Medical", sku="MED124", price=3.0, stock=300),
    Product(name="Latex Gloves Box", category="Medical", sku="MED456", price=15.0, stock=300),
    Product(name="Nitrile Gloves Box", category="Medical", sku="MED457", price=18.0, stock=200),
    Product(name="Surgical Mask Pack", category="PPE", sku="PPE789", price=10.0, stock=1000),
    Product(name="Face Shield", category="PPE", sku="PPE790", price=5.0, stock=150),
    Product(name="Digital Thermometer", category="Equipment", sku="EQ123", price=25.0, stock=100),
    Product(name="Pulse Oximeter", category="Equipment", sku="EQ124", price=45.0, stock=80),
    Product(name="Stethoscope", category="Equipment", sku="EQ125", price=60.0, stock=50),
]

db.add_all(products)
db.commit()
db.close()
print("Sample products added!")
