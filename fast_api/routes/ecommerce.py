from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from config.database import engine, get_db
from ecommerce import models, crud, schemas

models.Base.metadata.create_all(bind=engine)
router = APIRouter()


@router.get("/products/", tags=["products"])
async def read_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.get("/products/{product_id}", tags=["products"])
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/products/", response_model=schemas.Product, tags=["products"])
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db=db, product=product)


@router.post("/orders/", response_model=schemas.Order, tags=["products"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@router.post("/categories/", response_model=schemas.Category, tags=["products"]) # noqa
def create_order(category: schemas.CategoryCreate, db: Session = Depends(get_db)): # noqa
    return crud.create_category(db=db, category=category)
