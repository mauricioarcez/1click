from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI()

# Incluir rutas de autenticación
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
