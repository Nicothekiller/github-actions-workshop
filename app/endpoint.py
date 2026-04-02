from app.calculator import sum, multiply, resta
from pydantic import BaseModel
from fastapi import FastAPI


class Base(BaseModel):
    pass


class CalcRequest(Base):
    a: int
    b: int


class CalcResponse(Base):
    a: int


app = FastAPI()


@app.post("/suma", response_model=CalcResponse)
def post_suma(request: CalcRequest) -> CalcResponse:
    return CalcResponse(a=sum(request.a, request.b))


@app.post("/resta", response_model=CalcResponse)
def post_resta(request: CalcRequest) -> CalcResponse:
    return CalcResponse(a=resta(request.a, request.b))


@app.post("/multiplicacion", response_model=CalcResponse)
def post_multiplicacion(request: CalcRequest) -> CalcResponse:
    return CalcResponse(a=multiply(request.a, request.b))
