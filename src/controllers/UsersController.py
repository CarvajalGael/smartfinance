from models.userModel import UsuarioModel
from models.schemasModel import UsuarioLogin
from pydantic import ValidationError


class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, correo, password):

        try:
            nuevo_usuario = UsuarioNuevo(
                nombre=nombre,
                correo=correo,
                password=password
            )

            success = self.model.registrar(nuevo_usuario)

            if success:
                return True, "Usuario creado correctamente"
            else:
                return False, "Error al crear usuario"

        except ValidationError as e:
            return False, e.errors()[0]['msg']

    def login(self, correo, password):

        try:
            usuario_login = UsuarioLogin(
                email=correo,
                password=password
            )

            usuario_encontrado = self.model.iniciar_sesion(usuario_login)

            if usuario_encontrado:
                return usuario_encontrado, "Inicio de sesión exitoso"

            return None, "Correo o contraseña incorrectos"

        except Exception as e:
            print("ERROR EN LOGIN:", e)
            return None, "Error interno del servidor"