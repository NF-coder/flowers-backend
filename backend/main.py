'''
    Implementation of RESTful API
    
    For more info see docstrings in api directory!
'''

from settings import MainConfig

from fastapi import FastAPI, Query, HTTPException, Request, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# from typing import Dict, Any
# from datetime import datetime

from api import *
from exceptions import BasicException

# -- INIT BLOCK --

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(admin.router)
# app.include_router(moex_info.router)

# -- MAIN BLOCK --

@app.exception_handler(BasicException)
async def basicException_handler(request: Request, exc: BasicException) -> JSONResponse:
    '''
        Function, which catches BasicException and sends info about it to client
        Args:
            request (Request):
                Not used, but requried argument. Contains data about request
            exc (BasicException):
                A dataclass with data about exception (`code` and `description`)
        Returns:
            obj (JSONResponse): 
                Data about error in json format
        
        ## Note
            DO NOT CALL IT DIRECTLY
            I used JSONResponse to set status code
    '''
    return JSONResponse(
        status_code=exc.code,
        content={
            "description": exc.description,
            "code": exc.code
        }
    )

@app.exception_handler(RequestValidationError)
async def validationException_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    '''
        Function, which catches ValidationError from pydantic and sends info about it to client
        Args:
            request (Request):
                Not used, but requried argument. Contains data about request
            exc (RequestValidationError):
                A class with data about exception
        Returns:
            obj (JSONResponse): 
                Data about error in json format
        
        ## Note
            DO NOT CALL IT DIRECTLY
            I used JSONResponse to set status code
    '''
    errors_string = ""
    for error in exc._errors:
        errors_string += rf"In {error['loc'][-1]}: {error['msg']}. "
    
    return JSONResponse(
        status_code=422,
        content={
            "description": errors_string[:-1:],
            "code": 422
        }
    )  

@app.get(f'/api/v{MainConfig.API_VERSION}/ping', status_code = 200)
async def send():
    '''
        GET request to test avilability of server. See in /api/ping
    '''
    return {"status": "ok"}

if __name__ == "__main__": app.run()