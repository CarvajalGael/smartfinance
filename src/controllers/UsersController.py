from database import Database

class AuthController:

    def login(self, correo, contraseña):

        conexion = Database.get_connection()

        try:
            cursor = conexion.cursor(dictionary=True)

            sql = """
            SELECT * FROM usuarios
            WHERE correo=%s AND contraseña=%s
            """

            cursor.execute(sql, (correo, contraseña))
            usuario = cursor.fetchone()

            if usuario:
                return usuario, None
            else:
                return None, "Correo o contraseña incorrectos"

        except Exception as e:
            return None, f"Error: {str(e)}"

        finally:
            conexion.close()