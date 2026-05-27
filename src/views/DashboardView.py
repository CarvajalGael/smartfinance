import flet as ft

def DashboardView(page, auth_controller):

    mensaje = ft.Text(
        "Selecciona una opción",
        size=20,
        weight=ft.FontWeight.BOLD
    )

    return ft.View(
        route="/dashboard",

        controls=[
            ft.AppBar(
                title=ft.Text("Control Financiero"),
                center_title=True
            ),

            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,

                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,

                    controls=[
                        mensaje,

                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,

                            controls=[
                                ft.ElevatedButton(
                                    "Ingreso",
                                    icon=ft.Icons.ATTACH_MONEY,
                                    bgcolor=ft.Colors.GREEN,
                                    color=ft.Colors.WHITE,
                                    width=150,
                                    height=50,
                                    on_click=lambda e: page.go("/ingreso")
                                ),

                                ft.ElevatedButton(
                                    "Gastos",
                                    icon=ft.Icons.MONEY_OFF,
                                    bgcolor=ft.Colors.RED,
                                    color=ft.Colors.WHITE,
                                    width=150,
                                    height=50,
                                    on_click=lambda e: page.go("/gastos")
                                ),
                            ]
                        )
                    ]
                )
            )
        ]
    )