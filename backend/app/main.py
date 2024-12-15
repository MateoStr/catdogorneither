#script to start the back end server

#To run from terminal for testing: uvicorn app.main:app --reload

from fastapi import FastAPI
from app.routers import image_router

app = FastAPI()

#include the router for image processing
#app.include_router(image_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Backend!"}