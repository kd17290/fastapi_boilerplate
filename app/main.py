# LICENSE HEADER
from dotenv import load_dotenv
from fastapi import FastAPI

from app.core.main_router import router as healthcheck_router

load_dotenv('.env')

app = FastAPI(title='Demo MS')

app.include_router(healthcheck_router)
