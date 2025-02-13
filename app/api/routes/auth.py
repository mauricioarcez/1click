from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from app.core.security import create_access_token, verify_password, hash_password

router = APIRouter()

# Simulación de base de datos (esto se reemplazará con Firestore o SQL)
fake_users_db = {
    "test@example.com": {
        "email": "test@example.com",
        "hashed_password": hash_password("123456"),
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Autenticación de usuario y generación de token JWT"""
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    
    token = create_access_token(data={"sub": user["email"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register")
def register(email: str, password: str):
    """Registro de usuario (simulado, luego se integrará con Firestore)"""
    if email in fake_users_db:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    fake_users_db[email] = {"email": email, "hashed_password": hash_password(password)}
    return {"message": "Usuario registrado con éxito"}
