from fastapi import Depends, APIRouter
from product.schemas import Product
from product.repository import ProductRepository

router = APIRouter()

@router.get("/{pk}")
def get_product(pk: int, repository: ProductRepository = Depends(ProductRepository)):
    return repository.get_product(pk=pk)

