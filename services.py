import email_validator as _email_validator
from fastapi import HTTPException, status
import database as _database
import models as _models
import schemas as _schemas
import sqlalchemy.orm as _orm


def create_db():
    return _database.Base.metadata.create_all(bind=_database.engine)


# create_db()


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.UserModel).filter(_models.UserModel.email == email).first()


async def create_user(user: _schemas.UserRequest, db: _orm.Session):
    # check email format
    try:
        isValid = _email_validator.validate_email(email=user.email)
        email = isValid.email
    except _email_validator.EmailNotValidError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="email is not in correct format")
