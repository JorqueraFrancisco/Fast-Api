from fastapi import (
    Depends,
    HTTPException,
    APIRouter
)
from users.schemas import (
    UserCreate,
    User
)
from sqlalchemy.orm import Session
from config.database import engine, get_db
from users import models, crud


models.Base.metadata.create_all(bind=engine)
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@router.get("/users/{user_id}", tags=["users"])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=400, detail="user not found")
    return user


@router.post("/users/", response_model=User, tags=["users"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
