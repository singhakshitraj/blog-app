from fastapi import APIRouter,Depends,HTTPException,status
from db.connection import db_connection
from db.models import Blogs,Account
from utils.validation_models import BlogCreationValidation
import psycopg2
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix='/blogs'
)

@router.post('/')
def createblog(blog:BlogCreationValidation,session=Depends(db_connection)):
    try:
        new_blog= Blogs(title=blog.title,content=blog.content,account_id=blog.account_id)
        session.add(new_blog)
        session.commit()
        return JSONResponse(status_code=201,content='Created!')
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='Account Referenced does not exist or has been deleted!.')
    
@router.get('/')
def getAllblogs(session=Depends(db_connection)):
    try:
        cmd = select(Blogs).options(joinedload(Blogs.account_details))
        blogs = session.execute(cmd).scalars().all()
        return {
            'data':blogs
        }
    except psycopg2.DatabaseError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,detail='Something wrong with DB.')