import flet as ft

def RegistroView(page, auth_controller):


    nombre_input = ft.TextField(
        label="Nombre",
        hint_text="Ingresa tu nombre",
        width=350,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.PERSON,
    )

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

    dialogo = ft.AlertDialog(
        title=ft.Text("Error de registro"),
        content=ft.Text(""),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: cerrar_dialogo())
        ]
    )

    def cerrar_dialogo():
        dialogo.open = False
        page.update()

    def validar_campos():
        return bool(
            nombre_input.value.strip() and
            email_input.value.strip() and
            password_input.value.strip()
        )

    def registrar_usuario(e):
        if not validar_campos():
            page.snack_bar = ft.SnackBar(
                ft.Text("Completa los campos obligatorios")
            )
            page.snack_bar.open = True
            page.update()
            return

        success, mensaje = auth_controller.registrar_usuario(
            nombre_input.value.strip(),
            email_input.value.strip(),
            password_input.value.strip()
        )

        if success:
            page.snack_bar = ft.SnackBar(
                ft.Text(mensaje)
            )
            page.snack_bar.open = True
            page.update()
            page.go("/dashboard")
        else:
            dialogo.content = ft.Text(mensaje)
            dialogo.open = True
            page.dialog = dialogo
            page.update()


    boton_registrar = ft.ElevatedButton(
        "Registrar usuario",
        width=350,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        on_click=registrar_usuario
    )

    return ft.View(
        route="/registro",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Crear cuenta",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),
                    nombre_input,
                    email_input,
                    password_input,
                    boton_registrar,
                    ft.TextButton(
                        "Volver al login",
                        on_click=lambda e: page.go("/")
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )