from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore

app = FastAPI()

# Initialize Firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Define the Post model
class Post(BaseModel):
    title: str
    content: str

# Create a new post
@app.post("/posts/", response_model=Post)
def create_post(post: Post):
    post_ref = db.collection("posts").document()
    post_data = post.dict()
    post_ref.set(post_data)
    return 'post created Successfully' 

# Get a list of all posts
@app.get("/posts/", response_model=dict)
def get_posts():
    posts_ref = db.collection("posts")
    posts = [{"id": doc.id, **doc.to_dict()} for doc in posts_ref.stream()]
    return {"posts": posts}

# Delete a post
@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    post_ref = db.collection("posts").document(post_id)
    post_ref.delete()
    return "Post deleted successfully"
@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: str, updated_post: Post):
    post_ref = db.collection("posts").document(post_id)
    post = post_ref.get()
    
    if post.exists:
        # Update the post with the new data
        post_ref.update(updated_post.dict())
        return updated_post
    raise HTTPException(status_code=404, detail="Post not found")


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
