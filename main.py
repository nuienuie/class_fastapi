from fastapi import FastAPI

app = FastAPI()


@app.get("/get_test")
def test():
    return {"Hello": "get"}


@app.post("/post_test")
def test():
    return {"Hello": "post"}