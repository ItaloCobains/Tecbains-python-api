from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tecbains.router.user_router import router as user_router
from fastapi.security import HTTPBearer
from tecbains.middleware.get_user_by_token import get_user_by_token

app = FastAPI()
security = HTTPBearer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router.router, prefix="/user", tags=["user"])

@app.get("/")
async def secure_route(user_id: int = Depends(get_user_by_token)):
    return {"user_id": user_id}