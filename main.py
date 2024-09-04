from fastapi import FastAPI,Depends, HTTPException,Request 
import uvicorn
from typing import Any
from typing import Optional,List 
from pydantic import BaseModel 
from fastapi.responses import JSONResponse
from models import Car
from engine import engine
from sqlmodel import Session
from pydantic import BaseModel

app = FastAPI(docs_url="/docs")

def get_session():
    with Session(engine) as session:
        yield session

@app.post("/createCar", response_model=Car)
def create_car(car: Car, session: Session = Depends(get_session)):
    new_car = Car(make=car.make, model=car.model, year=car.year)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080,reload=True)
