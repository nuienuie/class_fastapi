from fastapi import FastAPI, Depends, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(docs_url='/v1/docs', redoc_url='/v1/redoc')


@app.get("/get_test")
def test():
    return {"Hello": "get"}


@app.post("/post_test")
def test():
    return {"Hello": "post"}


class login_data(BaseModel):
    id: str
    pw: str
    is_guest: Optional[bool] = False


admin_info = {
    'id': 'admin',
    'pw': '1234',
}


@app.post('/login')
def login(data: login_data = Depends()):
    # 전역변수로 지정된 id 값과 일치하면 통과
    if data.id == admin_info['id']:
        # 전역변수로 지정된 pw 값과 일치하면 통과
        if data.pw == admin_info['pw']:
            return 'success'
        else:
            return 'password_error'
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='denied')