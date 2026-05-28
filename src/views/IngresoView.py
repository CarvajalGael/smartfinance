import flet as ft

def IngresosView(page, auth_controller):

    ingreso_editando = {"id": None}

    ingreso_input = ft.TextField(
        label="Ingreso",
        hint_text="Ingresa el ingreso",
        width=350,
        border=ft.InputBorder.NONE,
        prefix_icon=ft.Icon(ft.Icons.ATTACH_MONEY),
        keyboard_type=ft.KeyboardType.NUMBER,
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

    tabla_ingresos = ft.Column()
    usuario = auth_controller.usuario_actual 

    def validar_campos():
        return bool(
            ingreso_input.value.strip() and
            descripcion_input.value.strip()
        )

    def cargar_ingresos():
        tabla_ingresos.controls.clear()
        ingresos = auth_controller.obtener_ingresos()
        for ingreso in ingresos:

            tarjeta = ft.Container(
                width=350,
                padding=15,
                border_radius=10,
                bgcolor=ft.Colors.GREEN_50,

                content=ft.Column(
                    controls=[

                        ft.Text(
                            f"Ingreso: ${ingreso['monto']}",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            f"Descripción: {ingreso['descripcion']}"
                        ),

                        ft.Text(
                            f"Fecha: {ingreso['fecha']}"
                        ),

                        ft.Row(
                            controls=[

                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    icon_color=ft.Colors.BLUE,
                                    on_click=lambda e, i=ingreso: editar_ingreso(i)
                                ),

                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color=ft.Colors.RED,
                                    on_click=lambda e, id=ingreso["id_ingreso"]: eliminar_ingreso(id)
                                )
                            ]
                        )
                    ]
                )
            )

            tabla_ingresos.controls.append(tarjeta)

        page.update()

    def limpiar_campos():
        ingreso_input.value = ""
        descripcion_input.value = ""
        ingreso_editando["id"] = None

    def guardar_ingreso(e):
        if not validar_campos():
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Completa todos los campos")
            )
            page.snack_bar.open = True
            page.update()
            return

        monto = ingreso_input.value
        descripcion = descripcion_input.value

        if ingreso_editando["id"] is None:
            auth_controller.crear_ingreso(
                usuario["id_usuario"], 
                monto,
                descripcion
            )
            mensaje = "Ingreso guardado correctamente"
        else:
            auth_controller.actualizar_ingreso(
                ingreso_editando["id"],
                monto,
                descripcion
            )
            mensaje = "Ingreso actualizado correctamente"

        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje)
        )
        page.snack_bar.open = True

        limpiar_campos()
        cargar_ingresos()

    def editar_ingreso(ingreso):
        ingreso_editando["id"] = ingreso["id_ingreso"]
        ingreso_input.value = str(ingreso["monto"])
        descripcion_input.value = ingreso["descripcion"]
        page.update()
        
    def eliminar_ingreso(id_ingreso):
        auth_controller.eliminar_ingreso(id_ingreso)
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Ingreso eliminado correctamente")
        )
        page.snack_bar.open = True
        cargar_ingresos()

    boton_guardar = ft.ElevatedButton(
        content=ft.Text("Guardar ingreso"),
        width=350,
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.WHITE,
        icon=ft.Icons.SAVE,
        on_click=guardar_ingreso
    )

    cargar_ingresos()

    return ft.View(
        route="/ingreso",
        scroll=ft.ScrollMode.AUTO,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        controls=[

            ft.Column(
                controls=[

                    ft.Text(
                        "Registrar ingresos",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),

                    ingreso_input,
                    descripcion_input,

                    boton_guardar,

                    ft.Divider(),

                    tabla_ingresos,

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