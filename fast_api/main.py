from fastapi import FastAPI, UploadFile
from routes import users, ecommerce, login
app = FastAPI()

app.include_router(users.router)
app.include_router(ecommerce.router)
app.include_router(login.router)


@app.post("/uploadfile/")
async def create_upload_file(file: list[UploadFile]):
    return {"filename": file.filename}


@app.get("/")
def read_root():
    return {"Hello": "World"}
