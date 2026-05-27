import bcrypt
from .databaseModel import Database
class UsuarioModel:

    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):

        salt = bcrypt.gensalt()

        hashed_pw = bcrypt.hashpw(
            usuario_data.password.encode('utf-8'),
            salt
        )

        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO usuarios
                (nombre, correo, password)
                VALUES (%s, %s, %s)
            """

            values = (
                usuario_data.nombre,
                usuario_data.correo,
                hashed_pw.decode('utf-8')
            )

            cursor.execute(query, values)
            conn.commit()

            return True

        except Exception as e:
            print("ERROR REGISTRO:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def iniciar_sesion(self, usuario_data):

        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM usuarios WHERE correo=%s"
            cursor.execute(query, (usuario_data.email,))
            usuario = cursor.fetchone()

            if usuario:

                pw_input = usuario_data.password.encode('utf-8')
                pw_db = usuario['password'].encode('utf-8')

                if bcrypt.checkpw(pw_input, pw_db):
                    return usuario

            return None

        except Exception as e:
            print("ERROR LOGIN:", e)
            return None

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()