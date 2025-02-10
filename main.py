from typing import Union

from ddtrace import tracer
from fastapi import FastAPI

app = FastAPI()


class BadException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        raise Exception("cant make into string")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@tracer.wrap()
async def inner_method():
    raise BadException("this is a bad exception")


@app.get("/error")
async def error():
    await inner_method()
