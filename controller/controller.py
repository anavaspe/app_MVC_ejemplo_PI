from fastapi import FastAPI, Request, Response, Body
from fastapi.responses import RedirectResponse
from firebase_admin import auth
from fastapi.staticfiles import StaticFiles
from view.view import View
from model.model import Model

import json
from pathlib import Path

from model.dao.firebase.firebaseDAOFactory import FirebaseDAOFactory

BASE_DIR = Path(__file__).resolve().parent

#Inicialización de FastAPI
app = FastAPI()

myviewcomponent = View()
mymodelcomponent = Model(factory=FirebaseDAOFactory())

#Sesiones de usuario, se guardarán en un diccionario con el formato {uid: user_data}
sessions = {}

@app.get("/")
async def index(request: Request):
    return myviewcomponent.get_index_view(request)

@app.get("/login")
async def login(request: Request):
    return myviewcomponent.get_login_view(request)

@app.get("/signup")
async def signup(request: Request):
    return myviewcomponent.get_signup_view(request)

@app.get("/cliente_view")
async def cliente_view(request: Request):
    return myviewcomponent.get_client_view(request)

@app.post("/login-password")
async def login_password(data: dict = Body(...)):
    idtoken = data.get("token")

    #Verificar el token con la librería de Firebase
    #Si el token es valido creamos la sesion del usuario y lo redirigimos a la interfaz de administrador
    decoded_token = auth.verify_id_token(idtoken)

    uid = decoded_token['uid']
    email = decoded_token['email']

    print(uid, email)
    #Comprobamos si dicho usuario tiene una sesión creada, y si no la tiene se la creamos
    user = mymodelcomponent.get_usuario(uid)

    if user is not None and not user.is_Empty():
        # Guardar el usuario en la sesión
        user_json = user.user_to_json()
        print(f"Guardando en sesión: {user_json}")
        sessions[uid] = user.get_sesion()  #Guardar solo los datos necesarios para la sesión

        if user.get_role() == "administrador":
            redirect = RedirectResponse(url="/administrador_view", status_code=303)
            redirect.set_cookie(key="session", value=uid, httponly=True)
        else:
            RedirectResponse(url="/", status_code=303)
        return redirect

@app.get("/administrador_view")
async def administrador_view(request: Request):
    #Aquí se debería verificar que el usuario tiene una sesión activa, y si no la tiene redirigirlo al login
    #Si el usuario tiene una sesión activa, se le debería mostrar la interfaz de administrador con los pedidos obtenidos desde el modelo
    cookie = request.cookies.get("session")
    print(cookie)
    user = sessions.get(cookie)
    if user is None:
        return RedirectResponse(url="/login", status_code=303)
    
    pedidos = json.loads(mymodelcomponent.get_pedidos())
    data = {
        "pedidos": pedidos
    }
    return myviewcomponent.get_administrador_view(request, data)

app.mount("/", StaticFiles(directory="/home/navas/Escritorio/Venias/PI_2025_2026/EjemploFastAPI/view/static", html=True), name="static")