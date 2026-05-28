import flet as ft

def GastosView(page, auth_controller):

    monto_input = ft.TextField(
        label="Monto",
        hint_text="Ingresa el monto",
        width=350,
        border=ft.InputBorder.NONE,
        prefix_icon=ft.Icon(ft.Icons.ATTACH_MONEY),
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    categoria_input = ft.TextField(
        label="Categoría",
        hint_text="Ingresa la categoría",
        width=350,
        border=ft.InputBorder.NONE,
        prefix_icon=ft.Icon(ft.Icons.CATEGORY),
    )

    descripcion_input = ft.TextField(
        label="Descripción",
        hint_text="Ingresa la descripción",
        width=350,
        border=ft.InputBorder.NONE,
        multiline=True,
        min_lines=2,
        max_lines=4,
        prefix_icon=ft.Icon(ft.Icons.DESCRIPTION),
    )

    def validar_campos():
        return bool(
            monto_input.value.strip() and
            categoria_input.value.strip() and
            descripcion_input.value.strip()
        )

    def guardar_gasto(e):

        if not validar_campos():

            page.snack_bar = ft.SnackBar(
                content=ft.Text("Completa todos los campos")
            )

            page.snack_bar.open = True
            page.update()
            return

        print(
            monto_input.value,
            categoria_input.value,
            descripcion_input.value
        )

        page.snack_bar = ft.SnackBar(
            content=ft.Text("Gasto guardado correctamente")
        )

        page.snack_bar.open = True

        monto_input.value = ""
        categoria_input.value = ""
        descripcion_input.value = ""

        page.update()

    boton_guardar = ft.ElevatedButton(
        content=ft.Text("Guardar gasto"),
        width=350,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        icon=ft.Icons.SAVE,
        on_click=guardar_gasto
    )

    return ft.View(
        route="/gastos",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[

                    ft.Text(
                        "Registrar gasto",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),

                    monto_input,
                    categoria_input,
                    descripcion_input,

                    boton_guardar,

                    ft.TextButton(
                        content=ft.Text("Volver al inicio"),
                        on_click=lambda e: page.go("/dashboard")
                    ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )