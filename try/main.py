from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK

cred = credentials.Certificate('firebase-credentials.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://crud-21696-default-rtdb.firebaseio.com'
})

app = FastAPI()

# Define a Pydantic model for user registration data

class UserRegistration(BaseModel):
    username: str
    password: str

# Create a route for user registration
@app.post("/signup")
async def signup(user_data: UserRegistration):
    try:
        # Check if the user already exists
        
        existing_user = db.reference('users').order_by_child('username').equal_to(user_data.username).get()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        # Create a new user in the Firebase Realtime Database

        new_user = {
            'username': user_data.username,
            'password': user_data.password
        }
        user_ref = db.reference('users').push(new_user)
        user_id = user_ref.key

        return {"user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
