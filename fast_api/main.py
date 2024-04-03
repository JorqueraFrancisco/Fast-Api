from fastapi import FastAPI
from routes import users

app = FastAPI()

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/product/{id_product}")
def create_product(id_product: int):
    return id_product
