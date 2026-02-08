from pydantic import BaseModel

class AccountCreationValidation(BaseModel):
    name : str
    
class BlogCreationValidation(BaseModel):
    title:str
    content:str
    account_id:int