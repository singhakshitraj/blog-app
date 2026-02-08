from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import String,Integer,ForeignKey
from typing import Optional


class Base(DeclarativeBase):
    pass

class Account(Base):
    __tablename__ = 'account'
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(40),nullable=False)
    
    blogs : Mapped[list['Blogs']] = relationship(back_populates='account_details')
    
class Blogs(Base):
    __tablename__ = 'blogs'
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    title : Mapped[str] = mapped_column(String(50),nullable=False)
    content : Mapped[str] = mapped_column(String(100),nullable=False)
    account_id : Mapped[int] = mapped_column(ForeignKey('account.id'),nullable=False)
    
    account_details: Mapped['Account']=relationship(back_populates='blogs')