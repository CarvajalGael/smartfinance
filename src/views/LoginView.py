import flet as ft

def LoginView(page, auth_controller):

    email_input = ft.TextField(
        label="Correo",
        hint_text="Ingresa tu correo",
        width=350,
        border=ft.InputBorder.NONE,
        prefix_icon=ft.Icons.EMAIL,
    )

    password_input = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa tu contraseña",
        width=350,
        password=True,
        can_reveal_password=True,
        border=ft.InputBorder.NONE,
        prefix_icon=ft.Icons.LOCK,
    )

    texto_error = ft.Text("", color=ft.Colors.RED)

    def cerrar_dialogo(e):
        dialogo.open = False
        page.update()

    def validar_campos():
        return bool(
            email_input.value.strip() and
            password_input.value.strip()
        )

    def mostrar_recuperacion(e):
        page.snack_bar = ft.SnackBar(
            ft.Text("Se envió un correo de recuperación")
        )
        page.snack_bar.open = True
        page.update()

    def hacer_login(e):

        if not validar_campos():
            page.snack_bar = ft.SnackBar(
                ft.Text("Completa todos los campos")
            )
            page.snack_bar.open = True
            page.update()
            return

        usuario, mensaje_error = auth_controller.login(
            email_input.value.strip(),
            password_input.value.strip()
        )

        if usuario:
            page.user_data = usuario
            page.go("/dashboard")

        else:
            texto_error.value = mensaje_error
            dialogo.open = True
            page.update()

    dialogo = ft.AlertDialog(
        title=ft.Text("Error de inicio"),
        content=texto_error,
        actions=[
            ft.TextButton(
                "Cerrar",
                on_click=cerrar_dialogo
            )
        ]
    )

    page.dialog = dialogo

    boton_login = ft.ElevatedButton(
        text="Iniciar sesión",
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
                    ft.Text(
                        "Login",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),

                    email_input,

                    password_input,

                    ft.TextButton(
                        "¿Olvidaste tu contraseña?",
                        on_click=mostrar_recuperacion
                    ),

                    boton_login,

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