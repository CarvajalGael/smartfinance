from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioLogin
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, apellido, email, password):
        try:
            nuevo_usuario=UsuarioNuevo(nombre=nombre, apellido=apellido, email=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            
            return False, e.errors()[0]['msg']
    
    def login(self, email, password):
            try:
                usuario_login = UsuarioLogin(email=email, password=password)
                usuario_encontrado = self.model.iniciar_sesion(usuario_login)
                if usuario_encontrado: 
                    return usuario_encontrado, "Inicio de sesión exitoso"
                else: 
                    return None, "Correo o contraseña incorrectos"
                    
            except Exception as e:
                print("ERROR EN LOGIN:", e)
                return None, f"Error: {str(e)}"