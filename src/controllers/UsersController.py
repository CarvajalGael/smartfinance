from models.userModel import UsuarioModel
from models.schemasModel import UsuarioLogin
from pydantic import ValidationError
from models.schemasModel import UsuarioNuevo

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

    def obtener_ingresos(self):
        return self.model.obtener_ingresos()

    def crear_ingreso(self, monto, descripcion):
        return self.model.crear_ingreso(monto, descripcion)

    def actualizar_ingreso(self, id_ingreso, monto, descripcion):
        return self.model.actualizar_ingreso(id_ingreso, monto, descripcion)

    def eliminar_ingreso(self, id_ingreso):
        return self.model.eliminar_ingreso(id_ingreso)

    def obtener_gastos(self):
        return self.model.obtener_gastos()

    def crear_gasto(self, monto, categoria, descripcion):
        return self.model.crear_gasto(monto, categoria, descripcion)

    def actualizar_gasto(self, id_gasto, monto, categoria, descripcion):
        return self.model.actualizar_gasto(id_gasto, monto, categoria, descripcion)

    def eliminar_gasto(self, id_gasto):
        return self.model.eliminar_gasto(id_gasto)