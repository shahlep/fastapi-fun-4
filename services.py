import database as _database
import models as _models
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


def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.UserModel).filter(_models.UserModel.email == email).first()
