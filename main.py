from fastapi import FastAPI

app = FastAPI(docs_url='/v1/docs', redoc_url='/v1/redoc')


@app.get("/get_test")
def test():
    return {"Hello": "get"}


@app.post("/post_test")
def test():
    return {"Hello": "post"}