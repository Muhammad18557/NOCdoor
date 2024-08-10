from fastapi import FastAPI
from app.routers import company

app = FastAPI()

app.include_router(company.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
