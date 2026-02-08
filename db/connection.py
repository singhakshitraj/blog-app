from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from utils.exceptions import DatabaseConnectionFailedException

load_dotenv()
url = os.getenv('DATABASE_URL') or None
if url is None:
    raise DatabaseConnectionFailedException

engine = create_engine(url=url)

session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def db_connection(): 
    try:
        new_session = session()
        yield new_session
    finally:
        new_session.close()