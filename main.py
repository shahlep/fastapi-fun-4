from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services

app = FastAPI()


@app.post("/users")
async def register_user(
    user: _schemas.UserRequest, db: _orm.Session = Depends(_services.get_db())
):
    db_user = await _services.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist"
        )
    # create the user and return a token


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
