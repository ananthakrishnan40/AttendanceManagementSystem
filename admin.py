from fastapi import APIRouter,Depends
from pydantic import BaseModel
from database import sessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import sessionLocal

router = APIRouter(prefix='/admin',tags=['Admin'])

def get_db():
    db = sessionLocal()
    try:
        yield db
    except Exception as e:
        print('Exception on markAttendence',e)
        raise
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

class Admin_login_validation(BaseModel):
    userName: str
    password: str


@router.post('/login')
async def checkadmin(credentials : Admin_login_validation,db:db_dependency):
    print('calling admin/login')
    data = db.execute(text('select * from user where User_Name = :userName and User_Password = :password'),
               {
                   'userName' : credentials.userName,
                   'password' : credentials.password 
               }).first()
    if data:
        print(data)
        return {'validation':True,
                'data':dict(data._mapping),
                'redirect':False,
                'nextpage':None}
    else:
        return {'validation':False,
                'redirect':False}


@router.get('/dashboard')
async def load_DashBoard(db:db_dependency):
    print('success')
    return 'success now need to create dashboard'    