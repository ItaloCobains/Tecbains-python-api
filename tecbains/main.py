from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tecbains.routes import (
    sign_up
)
from tecbains.dependencies.models import (DeclarativeBase)
from tecbains.dependencies.database import (
    engine
)

load_dotenv()

DeclarativeBase.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tecbains API",
    version="1.0.0",
    description="API for Tecbains",
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(sign_up.router)


