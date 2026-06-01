from models.userModel import UsuarioModel
from models.schemasModel import UsuarioLogin, UsuarioNuevo
from pydantic import ValidationError
import random
import string

from services.email_service import enviar_codigo


class AuthController:

    def __init__(self):
        self.model = UsuarioModel()
        self.usuario_actual = None

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
            print("VALIDATION ERROR:", e)
            return False, str(e)

        except Exception as ex:
            print("ERROR:", ex)
            return False, "Error interno"

    def enviar_codigo_recuperacion(self, correo, codigo):

        usuario = self.model.buscar_usuario_por_correo(correo)

        if not usuario:
            return False, "El correo no existe"

        try:
            enviar_codigo(correo, codigo)
            return True, "Código enviado al correo"

        except Exception as e:
            print("ERROR EMAIL:", e)
            return False, "No se pudo enviar el correo"

    def enviar_correo_olvido_contrasena(self, correo):

        usuario = self.model.buscar_usuario_por_correo(correo)

        if not usuario:
            return False, "El correo no existe"

        nueva_password = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=8
            )
        )

        actualizado = self.model.actualizar_password(
            correo,
            nueva_password
        )

        if actualizado:
            return True, f"Tu nueva contraseña es: {nueva_password}"

        return False, "No fue posible restablecer la contraseña"

    def restablecer_password(
        self,
        correo,
        codigo_ingresado,
        codigo_guardado,
        nueva_password
    ):

        usuario = self.model.buscar_usuario_por_correo(correo)

        if not usuario:
            return False, "El correo no existe"

        if str(codigo_ingresado) != str(codigo_guardado):
            return False, "Código incorrecto"

        actualizado = self.model.actualizar_password(
            correo,
            nueva_password
        )

        if actualizado:
            return True, "Contraseña actualizada correctamente"

        return False, "No fue posible actualizar la contraseña"

    def login(self, correo, password):

        try:
            usuario_login = UsuarioLogin(
                email=correo,
                password=password
            )

            usuario = self.model.iniciar_sesion(usuario_login)

            if usuario:
                self.usuario_actual = usuario
                return usuario, "Inicio de sesión exitoso"

            return None, "Correo o contraseña incorrectos"

        except Exception as e:
            print("ERROR LOGIN:", e)
            return None, "Error interno"

    def obtener_ingresos(self):
        return self.model.obtener_ingresos()

    def crear_ingreso(self, id_usuario, monto, descripcion):
        return self.model.crear_ingreso(
            id_usuario,
            monto,
            descripcion
        )

    def actualizar_ingreso(self, id_ingreso, monto, descripcion):
        return self.model.actualizar_ingreso(
            id_ingreso,
            monto,
            descripcion
        )

    def eliminar_ingreso(self, id_ingreso):
        return self.model.eliminar_ingreso(id_ingreso)

    def obtener_gastos(self):
        return self.model.obtener_gastos()

    def crear_gasto(
        self,
        id_usuario,
        monto,
        categoria,
        descripcion
    ):
        return self.model.crear_gasto(
            id_usuario,
            monto,
            categoria,
            descripcion
        )

    def actualizar_gasto(
        self,
        id_gasto,
        monto,
        categoria,
        descripcion
    ):
        return self.model.actualizar_gasto(
            id_gasto,
            monto,
            categoria,
            descripcion
        )

    def eliminar_gasto(self, id_gasto):
        return self.model.eliminar_gasto(id_gasto)
