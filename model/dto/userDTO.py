import json

class userDTO():
    def __init__(self):
        self.uid = None
        self.nombre = None
        self.email = None
        self.role = None
        self.sesion = None

    def is_Empty(self):
        return (self.uid is None and self.nombre is None and self.email is None and self.role is None and self.sesion is None)

    def get_uid(self):
        return self.uid

    def set_uid(self, uid):
        self.uid = uid

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_role(self):
        return self.role
    
    def set_role(self, role):
        self.role = role

    def get_sesion(self):
        return self.sesion
    
    def set_sesion(self, sesion):
        self.sesion = sesion

    def user_to_json(self):
        return json.dumps({
            "uid": self.uid,
            "nombre": self.nombre,
            "email": self.email,
            "role": self.role,
            "sesion": self.sesion
        })