from fastapi.templating import Jinja2Templates
from fastapi import Request


templates = Jinja2Templates(directory="view/templates")

class View ():
    def __init__(self):
        pass

    def get_index_view(self, request: Request):
        return templates.TemplateResponse("index.html", {"request": request})
    
    def get_login_view(self, request: Request):
        return templates.TemplateResponse("login.html", {"request": request})
    
    def get_signup_view(self, request: Request):
        return templates.TemplateResponse("signup.html", {"request": request})

    def get_administrador_view(self, request: Request, data: dict):
        return templates.TemplateResponse("interfaz-administrador.html", {"request": request, "data": data})