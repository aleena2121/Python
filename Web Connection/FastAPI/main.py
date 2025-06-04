from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10 ,published: bool=True, sort: Optional[str]=None):
    if published:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit} blogs from the database'}


@app.get('/blog/{id}')
def about(id: int):
    return {'data':id}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


@app.get('/blog/{id}/comments')
def comments(id, limit:int =10):
    return {'data':{ 3 , 2 }} 


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog Created with title {blog.title}'} 