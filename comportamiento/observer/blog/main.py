from blog import Blog
from suscriptor import SuscriptorEmail, SuscriptorSMS


def main():

    blog = Blog()

    suscriptor_email = SuscriptorEmail("juanperez@gmail.com")
    suscriptor_sms = SuscriptorSMS(2617007038)

    blog.agregar_suscriptor(suscriptor_email)
    blog.agregar_suscriptor(suscriptor_sms)

    titulo = "Nueva Receta de torta de limon publicada"
    blog.publicar(titulo)


    blog.eliminar_suscriptor(suscriptor_sms)

    titulo = "Nueva Receta de chocotorta publicada"
    blog.publicar(titulo)

if __name__ == "__main__":
    main()