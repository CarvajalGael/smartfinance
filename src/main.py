import flet as ft
from controllers.UsersController import AuthController
from views.LoginView import LoginView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.views.clear()
        
        if not page.views:
            page.views.append(ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacía")]))
        page.update()

    def view_pop(e):

        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = route_change

    page.go("/registro")
    route_change(page.route)

def main():
    ft.app(target=start)


if __name__ == "__main__":
    main()