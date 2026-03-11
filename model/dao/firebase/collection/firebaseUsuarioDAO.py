from ....dao.interfaceUsuarioDAO import InterfaceUsuarioDAO
from ....dto.userDTO import userDTO

class FirebaseUsuarioDAO(InterfaceUsuarioDAO):

    def __init__(self, user_doc):
        self.user_doc = user_doc
    
    def get_usuario(self, uid):
        user = userDTO()
        try:
            if self.user_doc is not None:
                user_data = self.user_doc.to_dict()  # Convierte el documento a un diccionario
                print(f"Datos del usuario desde Firebase: {user_data}")
                
                #Creamos la sesión y la introducimos en el DTO, para luego transformarlo a JSON y enviarlo al controlador
                sesion = {}
                sesion["uid"] = self.user_doc.id
                sesion["nombre"] = user_data.get("nombre", "")
                sesion["email"] = user_data.get("email", "")
                sesion["role"] = user_data.get("role", "")
                sesion["sesion"] = user_data.get("sesion", "")

                # Crear un objeto userDTO
                user = userDTO()
                user.set_uid(self.user_doc.id)  #Token del usuario
                user.set_nombre(user_data.get("nombre", ""))
                user.set_email(user_data.get("email", ""))
                user.set_role(user_data.get("role", ""))
                user.set_sesion(sesion)
                print(f"Usuario DTO creado: uid={user.get_uid()}, nombre={user.get_nombre()}")

                return user
            else:
                print(f"user_doc es None para uid: {uid}")
                return None
        except Exception as e:
            print(f"Error en get_usuario: {e}")
            return None