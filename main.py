from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount('/resources',StaticFiles(directory='templates/resources'))

@app.get('/')
async def check():
    result = open('templates/log_in.html')
    return HTMLResponse(result.read())
