from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI(docs_url='/v1/docs', redoc_url='/v1/redoc')


@app.get("/get_test")
def test():
    return {"Hello": "get"}


@app.post("/post_test")
def test():
    return {"Hello": "post"}


class login(BaseModel):
    id: str
    pw: str


@app.post('/login')
def login(data: login = Depends()):
    return data