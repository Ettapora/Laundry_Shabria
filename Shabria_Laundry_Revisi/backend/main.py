import bcrypt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import database, models, schemas

app = FastAPI(title="Shabria Laundry API")
models.Base.metadata.create_all(bind=database.engine)

# Setup CORS biar React (localhost:5173) bisa ngambil data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/api/auth/login")
def login(request: schemas.LoginRequest, db: Session = Depends(database.get_db)):
    # Cari user di database berdasarkan email
    user = db.query(models.User).filter(models.User.email == request.email).first()
    
    # Validasi email dan password (cocokin hash)
    if not user or not bcrypt.checkpw(request.password.encode('utf-8'), user.password.encode('utf-8')):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email atau password salah!"
        )
    
    # Kalau berhasil, kirim respons ke frontend
    return {
        "status": "success",
        "user_id": user.id_user,
        "nama": f"{user.first_name} {user.last_name or ''}".strip(),
        "role_id": user.id_role
    }

@app.get("/")
def read_root():
    return {"message": "Server Backend Shabria Laundry Nyala Bro!"}