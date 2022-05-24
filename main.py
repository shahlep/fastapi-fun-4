from fastapi import FastAPI, Depends
import uvicorn
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services

app = FastAPI()


@app.post('/users')
def register_user(user: _schemas.UserRequest,
                  db: _orm.Session = Depends(_services.get_db())):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
