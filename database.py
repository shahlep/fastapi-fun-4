import sqlalchemy as sqlalchemy
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

DB_URL = "sqlite:///./test.db"

engine = sqlalchemy.create_engine(DB_URL, connect_args={"check_same_thread": False})

SessionLocal = orm.sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative.declarative_base()
