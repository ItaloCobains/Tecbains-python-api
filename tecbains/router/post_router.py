from fastapi import APIRouter, Depends
from pytest import Session
from ..get_db import get_db

from tecbains.db.sqlite.schemas.post_schema import PostSchema
from ..use_cases.post_use_case import PostUseCase

postRouter = APIRouter()


@postRouter.post("/create", tags=["post"], summary="Create Post")
def create(post: PostSchema, db: Session = Depends(get_db)):

    postCase = PostUseCase(db)

    post = postCase.create(post)

    if not post:
        return None

    return post


@postRouter.get("/listAll", tags=["post"], summary="List All Posts")
def getAllPosts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):

    postCase = PostUseCase(db)

    posts = postCase.getAllPosts(skip=skip, limit=limit)

    return posts


@postRouter.get("/list/{id}", tags=["post"], summary="List Post By Id")
def getOnePost(db: Session = Depends(get_db), id: int = 0):

    postCase = PostUseCase(db)

    post = postCase.getOnePost(id)

    return post


@postRouter.get("/listByUser/{user_id}", tags=["post"], summary="List Posts By User Id")
def getPostsByUser(db: Session = Depends(get_db), user_id: int = 0):

    postCase = PostUseCase(db)

    posts = postCase.getPostsByUser(user_id)

    return posts


@postRouter.put("/update/{id}", tags=["post"], summary="Update Post By Id")
def updatePost(db: Session = Depends(get_db), id: int = 0, post: PostSchema = None):

    postCase = PostUseCase(db)

    post = postCase.update(id, post)

    return post

@postRouter.put("/like/{id}", tags=["post"], summary="Like Post By Id")
def likePost(db: Session = Depends(get_db), id: int = 0):

    postCase = PostUseCase(db)

    post = postCase.like(id)

    return post

@postRouter.delete("/delete/{id}", tags=["post"], summary="Delete Post By Id")
def deletePost(db: Session = Depends(get_db), id: int = 0):

    postCase = PostUseCase(db)

    post = postCase.delete(id)

    return post