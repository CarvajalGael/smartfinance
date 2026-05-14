import flet as ft

def LoginView(page, auth_controller):

    email_input = ft.TextField(
        label="Correo",
        hint_text="Ingresa tu correo",
        width=350,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.EMAIL,
    )

    password_input = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa tu contraseña",
        width=350,
        password=True,
        can_reveal_password=True,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.LOCK,
    )

    mensaje = ft.Text(
        "Se envió un correo de recuperación",
        visible=False,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLACK
    )

    def mostrar_mensaje(e):
        mensaje.visible = True
        page.update()

    def cerrar_dialogo(e):
        dialogo.open = False
        page.update()

    def validar_campos():
        return email_input.value and password_input.value

    def hacer_login(e):
        if not validar_campos():
            page.snack_bar = ft.SnackBar(ft.Text("Completa todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        usuario, mensaje_error = auth_controller.login(
            email_input.value,
            password_input.value
        )

        if usuario:
            page.user_data = usuario
            page.go("/dashboard")
        else:
            dialogo.content = ft.Text(mensaje_error)
            dialogo.open = True
            page.dialog = dialogo
            page.update()

    dialogo = ft.AlertDialog(
        title=ft.Text("Error de inicio"),
        content=ft.Text(""),
        actions=[ft.TextButton("Cerrar", on_click=cerrar_dialogo)]
    )

    boton_login = ft.ElevatedButton(
        "Iniciar sesión",
        width=350,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        on_click=hacer_login
    )

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
                    email_input,
                    password_input,
                    ft.TextButton("¿Olvidaste tu contraseña?", on_click=mostrar_mensaje),
                    boton_login,
                    mensaje,
                    ft.TextButton(
                        "Crear una nueva cuenta",
                        on_click=lambda e: page.go("/registro")
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )