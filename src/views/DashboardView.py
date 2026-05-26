import flet as ft

def DashboardView(page, auth_controller):

    def mostrar_mensaje(texto):
        mensaje.value = texto
        page.update()

    mensaje = ft.Text(
        "Selecciona una opción",
        size=20,
        weight="bold"
    )

    return ft.View(
        "/Dashboard",
        [
            ft.AppBar(
                title=ft.Text("Control Financiero"),
                center_title=True
            ),

            ft.Container(
                content=ft.Column(
                    [
                        mensaje,

                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Ingreso",
                                    icon=ft.icons.ATTACH_MONEY,
                                    bgcolor=ft.colors.GREEN,
                                    color=ft.colors.WHITE,
                                    width=150,
                                    height=50,
                                    on_click=lambda e: mostrar_mensaje("Botón INGRESO presionado")
                                ),

                                ft.ElevatedButton(
                                    "Gastos",
                                    icon=ft.icons.MONEY_OFF,
                                    bgcolor=ft.colors.RED,
                                    color=ft.colors.WHITE,
                                    width=150,
                                    height=50,
                                    on_click=lambda e: mostrar_mensaje("Botón GASTOS presionado")
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30
                ),
                expand=True,
                alignment=ft.alignment.center
            )
        ]
    )