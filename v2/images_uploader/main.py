'''
Unsafe, but fast to code module
'''
from fastapi import FastAPI, Query, HTTPException, Request, APIRouter, File
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from fastapi.responses import FileResponse

from typing import Annotated

import hashlib
from time import time_ns

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/file/{filename}', status_code = 200)
async def uploadImage(filename: str):
    return FileResponse(f"/images/{filename}.png")

@app.post('/upload', status_code = 200)
async def uploadImage(file: Annotated[bytes, File()]):
    hash=hashlib.sha3_224(file).hexdigest()

    with open("./images/"+str(hash)+".png", "wb+") as f:
        f.write(file)

    return {"path": "/api/v1/image/"+str(hash)}

if __name__ == "__main__":
    app.run()