from fastapi import FastAPI,Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from database import sessionLocal
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Annotated


app = FastAPI()




def get_db():
    db = sessionLocal()
    try:
        yield db
    except Exception as e:
        print('somthing went wrong with db connection......!!!!!!!!!!!',e)
        raise
    finally:
        db.close()





app.mount('/resources',StaticFiles(directory='templates/resources'))

@app.get('/')
async def check():
    result = open('templates/log_in.html')
    print('looding first log_in.html....')
    return HTMLResponse(result.read())


class AddUserValidation(BaseModel):
    pass


db_dependency = Annotated[Session,Depends(get_db)]


@app.post('/add_Employee')
async def addEmployee(db:db_dependency):
    print("Connection Database")
    data = {
        'Employee_Id' : 3,
        'Employee_Name' :'Appu',
        'Email_Id' :'appu@gmail.com',
        'Mobile_Number':'7994095129',
        'Department_Id':5,
        'Desigination':'DEV',
        'Added_By':1,
        'Employee_Password':'123',
        'Status':'ACTIVE'
        }
    db.execute(text("insert into employee(Employee_Id,Employee_Name,Email_Id,Mobile_Number,Department_Id,Desigination,Added_By,Added_at,Employee_Password,Status) values(:Employee_Id,:Employee_Name,:Email_Id,:Mobile_Number,:Department_Id,:Desigination,:Added_By,curdate(),:Employee_Password,:Status);"),data)
    db.commit()
    return 'sucess'
    
