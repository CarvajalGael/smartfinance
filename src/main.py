import flet as ft
from controllers.UsersController import AuthController
from views.LoginView import LoginView

#uv sync
def start(page: ft.Page):
    page.title="Sistema de inicio de sesion"
    page.window_width = 450
    page.window_height = 700
    
    auth_ctrl = AuthController()
    
    def route_change(e):
        page.views.clear()
        
        # caso 1: login
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
            
        #caso de seguridad    
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacia")])
            )
            
        page.update()
        
        
    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
    
    #1. asignar los manejadores de evento primero
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.user_data = None
    
    #2. IMPORTANTE, no fuerces page.route = ""
    print("Iniciando navegacion....")
    if page.route=="/":
        route_change(None)
    else:
        page.go("/")

def main():
    #ejecucion de la app
    ft.app(target=start)
    
if __name__ == "__main__":
    main()