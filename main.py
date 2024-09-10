from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body
class Calculation(BaseModel):
    a: float
    b: float

@app.post("/add/")
def add(calculation: Calculation):
    result = calculation.a + calculation.b
    return {"result": result}

@app.post("/subtract/")
def subtract(calculation: Calculation):
    result = calculation.a - calculation.b
    return {"result": result}

@app.post("/multiply/")
def multiply(calculation: Calculation):
    result = calculation.a * calculation.b
    return {"result": result}

@app.post("/divide/")
def divide(calculation: Calculation):
    if calculation.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = calculation.a / calculation.b
    return {"result": result}
