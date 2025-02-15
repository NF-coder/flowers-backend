'''
    Implementation of RESTful API
    
    For more info see docstrings in api directory!
'''

from settings import MainConfig

from fastapi import FastAPI, Query, HTTPException, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse
from typing import Dict, Any
from datetime import datetime

from api import *

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
# app.include_router(cb_info.router)
# app.include_router(moex_info.router)

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        code=exc.code,
        description=exc.output,
    )

# -- MAIN BLOCK --

@app.get('/api/ping', status_code = 200)
async def send():
    return {"status": "ok"}

if __name__ == "__main__": app.run()