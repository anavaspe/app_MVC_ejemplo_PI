# EjemploFastAPI

Aplicación web desarrollada con **FastAPI** que implementa un sistema de autenticación y gestión de pedidos, usando Firebase como backend y siguiendo una arquitectura **MVC** con patrón **DAO**.

---

## Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/) — framework web principal
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup) — autenticación y base de datos
- [Jinja2](https://jinja.palletsprojects.com/) — motor de plantillas HTML

---

## Estructura del proyecto

```
proyecto/
├── main.py                            # Punto de entrada
├── .gitignore
├── controller/
│   └── controller.py                  # Rutas y lógica de la aplicación (FastAPI)
├── model/
│   ├── model.py                       # Capa de modelo
│   ├── factory/
│   │   └── interfaceDAOFactory.py     # Interfaz abstracta del factory (Abstract Factory)
│   ├── dao/
│   │   ├── firebase/
│   │   │   ├── collection/            # Colecciones de Firestore
│   │   │   ├── credentials.json       # Credenciales de Firebase (⚠️ no subir a GitHub)
│   │   │   ├── firebaseConnector.py   # Conexión con Firebase
│   │   │   ├── firebaseDAOFactory.py  # Implementación concreta del factory
│   │   │   ├── interfacePedidosDAO.py # Interfaz DAO de pedidos
│   │   │   └── interfaceUsuarioDAO.py # Interfaz DAO de usuario
│   └── dto/
│       ├── pedidosDTO.py              # DTO de pedidos
│       └── userDTO.py                 # DTO de usuario
└── view/
    ├── view.py                        # Renderizado de plantillas
    ├── templates/
    │   ├── index.html
    │   ├── login.html
    │   ├── signup.html
    │   ├── interfaz_cliente.html
    │   └── interfaz-administrador.html
    └── static/
        ├── css/
        ├── js/
        └── images/
```

---

## Arquitectura

El proyecto sigue el patrón **MVC** desacoplado mediante el patrón **Abstract Factory** para los DAOs:

- **Controller** — gestiona las rutas HTTP y las sesiones de usuario.
- **Model** — obtiene los DAOs a través de la factory e implementa la lógica de negocio.
- **View** — renderiza las plantillas Jinja2 y sirve archivos estáticos.
- **InterfaceDAOFactory** — contrato abstracto que permite cambiar el backend de datos sin modificar el modelo.

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd EjemploFastAPI

# 2. Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn firebase-admin jinja2 python-multipart

# 3. Configurar Firebase
# Coloca tu archivo de credenciales de Firebase en el proyecto
# y asegúrate de inicializarlo en firebaseDAOFactory.py
```

---

## Uso

```bash
python main.py
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

---

## Rutas principales

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Página de inicio |
| `GET` | `/login` | Vista de login |
| `GET` | `/signup` | Vista de registro |
| `POST` | `/login-password` | Verificación de token Firebase |
| `GET` | `/cliente_view` | Panel de cliente (requiere sesión) |
| `GET` | `/administrador_view` | Panel de administrador (requiere rol) |

---

## Roles de usuario

- **cliente** — accede a `/cliente_view`.
- **administrador** — accede a `/administrador_view` y puede ver todos los pedidos.

La gestión de sesiones se realiza mediante cookies `httponly`.
