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

    def obtener_ingresos(self):

        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM ingresos"
            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:
            print("ERROR OBTENER INGRESOS:", e)
            return []

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_gastos(self):

        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM gastos"
            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:
            print("ERROR OBTENER GASTOS:", e)
            return []

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def crear_ingreso(self, id_usuario, monto, descripcion):

        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO ingresos (id_usuario, monto, descripcion)
                VALUES (%s, %s, %s)
            """

            cursor.execute(query, (id_usuario, monto, descripcion))
            conn.commit()

            return True

        except Exception as e:
            print("ERROR CREAR INGRESO:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def eliminar_ingreso(self, id_ingreso):

        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = "DELETE FROM ingresos WHERE id_ingreso = %s"

            cursor.execute(query, (id_ingreso,))
            conn.commit()

            return True

        except Exception as e:
            print("ERROR ELIMINAR INGRESO:", e)
            return False

        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()

    def actualizar_ingreso(self, id_ingreso, monto, descripcion):

        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                UPDATE ingresos
                SET monto = %s,
                    descripcion = %s
                WHERE id_ingreso = %s
            """

            cursor.execute(
                query,
                (
                    monto,
                    descripcion,
                    id_ingreso
                )
            )

            conn.commit()
            return True

        except Exception as e:
            print("ERROR ACTUALIZAR INGRESO:", e)
            return False

        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()

    def buscar_usuario_por_correo(self, correo):

        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
                SELECT *
                FROM usuarios
                WHERE correo = %s
            """

            cursor.execute(query, (correo,))
            return cursor.fetchone()

        except Exception as e:
            print("ERROR BUSCAR CORREO:", e)
            return None

        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()

    def actualizar_password(self, correo, nueva_password):

        conn = None
        cursor = None

        try:
            hashed_pw = bcrypt.hashpw(
                nueva_password.encode("utf-8"),
                bcrypt.gensalt()
            )

            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                UPDATE usuarios
                SET password = %s
                WHERE correo = %s
            """

            cursor.execute(
                query,
                (
                    hashed_pw.decode("utf-8"),
                    correo
                )
            )

            conn.commit()
            return True

        except Exception as e:
            print("ERROR ACTUALIZAR PASSWORD:", e)
            return False

        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()