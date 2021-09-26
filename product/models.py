from database import Base
from sqlalchemy import Column, Integer, String, Float


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    amount = Column(Integer)
