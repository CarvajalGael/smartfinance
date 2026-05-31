import flet as ft

def GastosView(page, auth_controller):
    gasto_editando = {"id": None}

    usuario = auth_controller.usuario_actual

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

    tabla_gastos = ft.Column()

    def validar_campos():
        return bool(
            monto_input.value.strip() and
            categoria_input.value.strip() and
            descripcion_input.value.strip()
        )

    def cargar_gastos():

        tabla_gastos.controls.clear()

        gastos = auth_controller.obtener_gastos()

        for gasto in gastos:

            tarjeta = ft.Container(
                width=350,
                padding=15,
                border_radius=10,
                bgcolor=ft.Colors.RED_50,

                content=ft.Column(
                    controls=[

                        ft.Text(
                            f"Gasto: ${gasto['monto']}",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            f"Categoría: {gasto['categoria']}"
                        ),

                        ft.Text(
                            f"Descripción: {gasto['descripcion']}"
                        ),

                        ft.Row(
                            controls=[

                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    icon_color=ft.Colors.BLUE,
                                    on_click=lambda e, g=gasto: editar_gasto(g)
                                ),

                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color=ft.Colors.RED,
                                    on_click=lambda e, id=gasto["id_gasto"]: eliminar_gasto(id)
                                )
                            ]
                        )
                    ]
                )
            )

            tabla_gastos.controls.append(tarjeta)

        page.update()

    def limpiar_campos():
        monto_input.value = ""
        categoria_input.value = ""
        descripcion_input.value = ""
        gasto_editando["id"] = None

    def guardar_gasto(e):

        if not validar_campos():

            page.snack_bar = ft.SnackBar(
                content=ft.Text("Completa todos los campos")
            )

            page.snack_bar.open = True
            page.update()
            return

        monto = monto_input.value
        categoria = categoria_input.value
        descripcion = descripcion_input.value

        if gasto_editando["id"] is None:

            auth_controller.crear_gasto(
    usuario["id_usuario"],
    monto,
    categoria,
    descripcion
)

            mensaje = "Gasto guardado correctamente"

        else:

            auth_controller.actualizar_gasto(
                gasto_editando["id"],
                monto,
                categoria,
                descripcion
            )

            mensaje = "Gasto actualizado correctamente"

        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje)
        )

        page.snack_bar.open = True

        limpiar_campos()
        cargar_gastos()

    def editar_gasto(gasto):

        gasto_editando["id"] = gasto["id_gasto"]

        monto_input.value = str(gasto["monto"])
        categoria_input.value = gasto["categoria"]
        descripcion_input.value = gasto["descripcion"]

        page.update()

    def eliminar_gasto(id_gasto):

        auth_controller.eliminar_gasto(id_gasto)

        page.snack_bar = ft.SnackBar(
            content=ft.Text("Gasto eliminado correctamente")
        )

        page.snack_bar.open = True

        cargar_gastos()

    boton_guardar = ft.ElevatedButton(
        content=ft.Text("Guardar gasto"),
        width=350,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        icon=ft.Icons.SAVE,
        on_click=guardar_gasto
    )

    cargar_gastos()

    return ft.View(
        route="/gastos",
        scroll=ft.ScrollMode.AUTO,
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

                    ft.Divider(),

                    tabla_gastos,

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