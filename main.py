from fastapi import FastAPI,Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from database import sessionLocal
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Annotated
import auth
import markAttendence
import admin

app = FastAPI()
app.include_router(auth.router)
app.include_router(markAttendence.router)
app.include_router(admin.router)


app.mount('/templates', StaticFiles(directory='templates'))

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


    
