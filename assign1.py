from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Pydantic model for blog posts
class Post(BaseModel):
    title: str
    content: str
    author: str

# In-memory storage for posts
posts = []

# FastAPI app initialization
app = FastAPI()

@app.post("/posts/", response_model=Post)
def create_post(post: Post):
    # Check for duplicate title
    if any(p["title"] == post.title for p in posts):
        raise HTTPException(status_code=400, detail="Post with this title already exists.")
    posts.append(post.dict())
    return post

@app.get("/posts/", response_model=List[Post])
def list_posts():
    return posts

@app.put("/posts/{title}", response_model=Post)
def update_post(title: str, updated_post: Post):
    for post in posts:
        if post["title"] == title:
            post.update(updated_post.dict())
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found.")

@app.delete("/posts/{title}")
def delete_post(title: str):
    for i, post in enumerate(posts):
        if post["title"] == title:
            del posts[i]
            return {"message": "Post deleted successfully."}
    raise HTTPException(status_code=404, detail="Post not found.")
