from fastapi import FastAPI,Depends,HTTPException
from fastapi.responses import JSONResponse
from db.connection import db_connection
from sqlalchemy import select,insert
from db.models import Blogs,Account
from utils.validation_models import AccountCreationValidation
from routers import blogs
from sqlalchemy.orm import selectinload

app = FastAPI()

app.include_router(blogs.router)

@app.get('/')
def fxn(session = Depends(db_connection)):
    cmd = select(Account).options(selectinload(Account.blogs))
    acc = session.execute(cmd).scalars().all()
    return {
        'data':acc
    }

@app.post('/')
def createaccount(account:AccountCreationValidation,session=Depends(db_connection)):
    try:
        acc = Account(name=account.name)
        session.add(acc)
        session.commit()
        return JSONResponse(status_code=201,content='Data Inserted!!')
    except Exception as e:
        raise HTTPException(status_code=401,detail=e.args)