from observador import Observador

class SuscriptorEmail(Observador):
    def __init__(self, email):
        self.email = email

    def actualizar(self, noticia):
        print(f"El suscriptor recibe la noticia: {noticia} a {self.email}")

class SuscriptorSMS(Observador):
    def __init__(self, telefono):
        self.telefono = telefono

    def actualizar(self, noticia):
        print(f"El suscriptor recibe la noticia: {noticia} a {self.telefono}")

