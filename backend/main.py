from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# Allow your Vercel frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://stackryo.vercel.app"], 
    allow_methods=["POST"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    password: str

@app.post("/verify-admin")
async def verify_admin(request: LoginRequest):
    # This reads from your Render environment variables
    correct_password = os.getenv("ADMIN_PASSWORD")
    
    if request.password == correct_password:
        return {"success": True, "token": "authenticated_session_started"}
    
    raise HTTPException(status_code=401, detail="Invalid password")