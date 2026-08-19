from fastapi import APIRouter,Depends
from pydantic import BaseModel
from database import sessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import sessionLocal
from fastapi.responses import HTMLResponse
import jose

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
        
        
# @router.post('/validate')
# def JWTvalidation(jwt):
    
    



@router.get('/dashboard')
async def load_DashBoard(db:db_dependency):
    print('success')
    html = open('templates/dashboard.html').read()
    return HTMLResponse(html)

class idvalidation(BaseModel):
    Employee_id:int


@router.post('/dashboard/searchbyid')
async def search_by_id(data:idvalidation,db:db_dependency):
       empId = data.Employee_id
       result = db.execute(text('select * from employee where Employee_ID = :employeeid'),{'employeeid':empId}).first()
       if result:
           return {
               'sucess':True,
               'data':dict(result._mapping)
               }
       else:
           return {'sucess':False}

class datevalidation(BaseModel):
    date : str
        
@router.post('/dashboard/presenttoday')
async def presenttoday(datedata:datevalidation,db:db_dependency):
    date = datedata.date
    print(date)
    data = db.execute(text('select E.Employee_Name as Name, E.Mobile_Number as Mobile, E.Email_Id, E.Department_Id as Department_Id, A.check_In_Time as Check_In, dep.Dept_Name as Department_Name , A.Attendence_Date from attendence A left join employee E on A.Employee_Id = E.Employee_Id left join department dep on E.Department_Id = dep.Dept_Id and A.Attendence_Date = curdate();')).all()
    if data:
        result = []
        for i in data:
            result.append(dict(i._mapping))
        return {
            'sucess': True,
            'data' : result
        }
    else:
        return {
            'sucess':False
        }

    