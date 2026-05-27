from pydantic import BaseModel, EmailStr

class UsuarioNuevo(BaseModel):
    nombre: str
    correo: EmailStr
    password: str

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str