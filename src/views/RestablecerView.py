import flet as ft
import random

codigo_global = {}

def RestablecerView(page, auth_controller):

    email_input = ft.TextField(
        label="Correo",
        hint_text="Ingresa tu correo",
        width=350,
        border=ft.InputBorder.NONE,
        prefix_icon=ft.Icon(ft.Icons.EMAIL),
    )

    codigo_input = ft.TextField(
        label="Código",
        hint_text="Ingresa el código recibido",
        width=350,
        border=ft.InputBorder.NONE,
        prefix_icon=ft.Icon(ft.Icons.VERIFIED_USER),
        disabled=True
    )

    new_password_input = ft.TextField(
        label="Nueva contraseña",
        hint_text="Ingresa tu nueva contraseña",
        width=350,
        password=True,
        can_reveal_password=True,
        border=ft.InputBorder.NONE,
        prefix_icon=ft.Icon(ft.Icons.LOCK),
        disabled=True
    )

    def enviar_codigo(e):

        correo = email_input.value.strip()

        if not correo:
            page.snack_bar = ft.SnackBar(content=ft.Text("Ingresa un correo"))
            page.snack_bar.open = True
            page.update()
            return

        codigo = random.randint(100000, 999999)

        codigo_global[correo] = str(codigo)

        exito, mensaje = auth_controller.enviar_codigo_recuperacion(
            correo,
            codigo
        )

        page.snack_bar = ft.SnackBar(content=ft.Text(mensaje))
        page.snack_bar.open = True

        if exito:
            codigo_input.disabled = False
            new_password_input.disabled = False

        page.update()

    def establecer(e):

        correo = email_input.value.strip()
        codigo_guardado = codigo_global.get(correo)

        if not codigo_guardado:
            page.snack_bar = ft.SnackBar(content=ft.Text("Primero solicita un código"))
            page.snack_bar.open = True
            page.update()
            return

        exito, mensaje = auth_controller.restablecer_password(
            correo,
            codigo_input.value.strip(),
            codigo_guardado,
            new_password_input.value.strip()
        )

        page.snack_bar = ft.SnackBar(content=ft.Text(mensaje))
        page.snack_bar.open = True
        page.update()

        if exito:
            codigo_global.pop(correo, None)
            page.go("/")

    boton_enviar_codigo = ft.ElevatedButton(
        content=ft.Text("Enviar código"),
        width=350,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        on_click=enviar_codigo
    )

    boton_guardar = ft.ElevatedButton(
        content=ft.Text("Restablecer contraseña"),
        width=350,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        on_click=establecer
    )

    return ft.View(
        route="/restablecer",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Restablecer contraseña", size=30, weight=ft.FontWeight.BOLD),
                    email_input,
                    boton_enviar_codigo,
                    codigo_input,
                    new_password_input,
                    boton_guardar,
                    ft.TextButton(
                        content=ft.Text("Volver al inicio"),
                        on_click=lambda e: page.go("/")
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )