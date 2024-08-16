from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional

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
    is_guest: Optional[bool] = False


@app.post('/login')
def login(data: dict = Depends(login)):
    return data