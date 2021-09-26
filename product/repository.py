from sqlalchemy.orm import Session
from database import SessionLocal
from product.models import Product


class ProductRepository:
    def __init__(self):
        self.db: Session = SessionLocal()
    
    def __del__(self):
        self.db.close()

    def get_product(self, pk: int):
        return self.db.query(Product).filter(Product.id == pk).first()

    def get_products(self):
        return self.db.query(Product).all()