# main.py

from fastapi import FastAPI, HTTPException
import firebase_admin
from firebase_admin import credentials, auth

app = FastAPI()

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase-admin-sdk.json")
firebase_admin.initialize_app(cred)

# Signup endpoint
@app.post("/signup")
async def signup(email: str, password: str):
    try:
        user = auth.create_user(email=email, password=password)
        return {"uid": user.uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Login endpoint
@app.post("/login")
async def login(email: str, password: str):
    try:
        user = auth.get_user_by_email(email)
        # You can add custom logic here to verify the password.
        return {"uid": user.uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
# GET request to retrieve user information by UID
@app.get("/user/{uid}")
async def get_user_by_uid(uid: str):
    try:
        user = auth.get_user(uid)
        # You can return additional user information as needed.
        return {"uid": user.uid, "email": user.email}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Update user email endpoint
@app.put("/user/{uid}")
async def update_user_email(uid: str, new_email: str):
    try:
        user = auth.get_user(uid)
        auth.update_user(uid, email=new_email)
        return {"message": "Email updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Delete user endpoint
@app.delete("/user/{uid}")
async def delete_user(uid: str):
    try:
        auth.delete_user(uid)
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))