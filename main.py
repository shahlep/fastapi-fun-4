from fastapi import FastAPI, Depends, HTTPException, status, security,Form
import uvicorn
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

app = FastAPI()


@app.post("/users")
async def register_user(
    user: _schemas.UserRequest, db: _orm.Session = Depends(_services.get_db)
):
    db_user = await _services.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist"
        )
    # create the user and return a token
    nw_user = await _services.create_user(user=user, db=db)
    return await _services.create_token(user=nw_user)


@app.post("/login")
async def login(
    form_data: security.OAuth2PasswordRequestForm = Depends(),
    db: _orm.Session = Depends(_services.get_db),
):
    db_user = await _services.login(
        email=form_data.username, password=form_data.password, db=db
    )
    # Invalid login then throw exception
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials!",
        )
    # create and return the token
    return await _services.create_token(db_user)


"""if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)"""

@app.post('/loginUser')
def login(username:str=Form(...), password:str=Form(...)):
    return {'username':username}
