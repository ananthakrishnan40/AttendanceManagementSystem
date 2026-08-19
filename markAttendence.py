from fastapi import APIRouter,Depends
from pydantic import BaseModel
from database import sessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import sessionLocal

router = APIRouter(prefix='/attendence',tags=['Attendence'])

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

class Idvalidation(BaseModel):
    Employee_Id : int

@router.post('/markAttendence')
async def markAttendence(id : Idvalidation,db:db_dependency):
    db.execute(text('insert into attendence(Employee_Id,Attendence_Date,Check_In_Time) values(:id,curdate(),current_time());'),{'id':id.Employee_Id})
    db.commit()
    print(f'Attendence of {id.Employee_Id} marked')
    return {'sucess':True}

