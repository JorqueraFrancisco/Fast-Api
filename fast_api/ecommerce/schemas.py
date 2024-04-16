from pydantic import BaseModel
from typing import List


class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class CategoryCreate(CategoryBase):
    pass


class Image(BaseModel):
    id: int
    product_id: int | None = None


class ImageBase(BaseModel):
    path: str

    class Config:
        from_attributes = True


class ImageCreate(ImageBase):
    pass


class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock_quantity: int
    category_id: None = None | int


class ProductCreate(ProductBase):
    images: List[ImageCreate]

    pass


class Product(ProductBase):
    id: int
    created_at: str | None = None

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    user_id: int
    status: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    created_at: str | None = None

    class Config:
        from_attributes = True


class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int

    class Config:
        from_attributes = True
