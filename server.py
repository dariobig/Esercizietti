from fastapi import FastAPI
from typing import Optional
from ripasso import chek_name, summation

app = FastAPI()


@app.get("/")
async def root(number: int, name: Optional[str] = 'world'):
    new_name = chek_name(name)
    if number and new_name == name:
        total = summation(number)
    return {"message": f"Hello {name} your summation is {total}"}

@app.get("/multiply")
async def multiply(a: int = 1, b: int = 1):
    return f"a: {a} x b {b} = {a * b}"