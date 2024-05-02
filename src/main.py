from fastapi import FastAPI

from src.core.router import router

app = FastAPI()

app.include_router(router, prefix='/api')
