from fastapi import APIRouter,Depends
from pydantic import BaseModel
from database import sessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter(prefix='/auth',tags=['authentication'])

def get_db():
    db = sessionLocal()
    try:
        yield db
    
    except Exception as e:
        print("somthing went wrong from auth database connection",e) 
        raise   
    finally:
        db.close()
    
    
db_dependency = Annotated[Session,Depends(get_db)]


class check_Employee_Validation(BaseModel):
    userName : str 
    password : str
    


@router.post('/check_Employee')
async def check_Employee(data : check_Employee_Validation , db: db_dependency):
    result = db.execute(text('select * from employee where Employee_Name = :userName and Employee_Password = :password'),data.model_dump()).first()
    print(data)
    if result:
        return {'valid':True,
                'Data':dict(result._mapping)}
    else:
        return {'valid' : False,
                'Data':result}