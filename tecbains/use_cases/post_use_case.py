from sqlalchemy.orm import Session
from ..db.sqlite.crud import (
    get_all_posts,
    get_post,
    create_post,
    delete_post,
    get_posts_by_user,
    update_post,
    like_post
)

class PostUseCase:
    def __init__(self, dbSession: Session):
        self.db: Session = dbSession
    
    def getAllPosts(self, skip: int = 0, limit: int = 100):
        posts = get_all_posts(self.db, skip, limit)
        return posts
    
    def getOnePost(self, post_id: int):
        post = get_post(self.db, post_id)
        return post
    
    def create(self, post):
        post = create_post(self.db, post)
        return post
    
    def delete(self, post_id: int):
        post = delete_post(self.db, post_id)
        return post
    
    def getPostsByUser(self, user_id: int):
        posts = get_posts_by_user(self.db, user_id)
        return posts
    
    def update(self, post_id: int, post):
        post = update_post(self.db, post_id, post)
        return post
    
    def like(self, post_id: int):
        post = like_post(self.db, post_id)
        return post
    