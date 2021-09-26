from fastapi import FastAPI
from product.models import Base as ProductBase
from product.main import router as product_routes
from database import engine
app = FastAPI()

ProductBase.metadata.create_all(bind=engine)
app.include_router(product_routes)