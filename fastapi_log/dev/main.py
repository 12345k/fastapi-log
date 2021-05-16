from log_request import LoggingRoute
from fastapi import Body, FastAPI, HTTPException, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import dashboard

app = FastAPI()
app.router.route_class = LoggingRoute
# Just add this one line
app.include_router(dashboard.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    userName: str
    age: str
    Degree: Optional[int] = None

@app.post("/test")
async def post_test(item:Item,response: Response):  
    return item

@app.get("/test1")
async def get_test1(response: Response):  
    return "test1"

@app.get("/test2")
async def get_test2(response: Response):  
    return "test2"

@app.get("/helloWorld")
async def get_test3(response: Response):  
    return "hello world"