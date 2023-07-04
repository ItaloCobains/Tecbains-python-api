from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tecbains.router.user_router import userRouter
from tecbains.router.post_router import postRouter
from .auth.auth_bearer import JWTBearer


load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(userRouter, prefix="/user", tags=["user"])
app.include_router(postRouter, prefix="/post", tags=["post"])


@app.get("/", dependencies=[Depends(JWTBearer())], tags=["root"])
async def root(token: str = Depends(JWTBearer())):
    return {"message": token}

