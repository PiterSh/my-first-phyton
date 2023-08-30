from fastapi import FastAPI

import service.serviceHellow

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/")
async def hello():
    return {"message": service.serviceHellow}
