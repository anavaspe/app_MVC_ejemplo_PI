from firebase_admin import credentials, firestore, initialize_app, auth

class FirebaseConnector ():
    firebase_app_initializated = False
    def __init__(self):
        self.db = None
        try:
            if not (FirebaseConnector.firebase_app_initializated):
                self.credentials = credentials.Certificate("model/dao/firebase/credentials.json")
                initialize_app(self.credentials)
            self.db = firestore.client()
            print("Connection to Firebase Firestore initialized successfully.")
            FirebaseConnector.firebase_app_initializated = True
        except Exception as e:
            print("Error in connecting with db")
            print(e)
            raise

    def get_db(self):
        if self.db is None:
            print("Database connection is not initialized.")
        return self.db

    def get_pedidos_collection(self):
        if self.db is None:
            print("Database connection is not initialized.")
        return self.db.collection("pedidos")
    
    def get_usuarios_collection(self):
        if self.db is None:
            print("Database connection is not initialized.")
        return self.db.collection("usuarios")
    
    def get_usuario_by_uid(self, uid):
        if self.db is None:
            print("Database connection is not initialized.")
        try:
            print(f"Buscando usuario con UID: {uid}")
            user_doc = self.db.collection("usuarios").document(uid).get()
            if user_doc.exists:
                print(f"Usuario encontrado: {user_doc.to_dict()}")
                return user_doc
            else:
                print(f"No user found with UID: {uid}")
                return None
        except Exception as e:
            print(f"Error fetching user with UID: {uid}")
            print(e)
            return None