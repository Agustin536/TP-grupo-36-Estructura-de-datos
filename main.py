#Main
from usuario import Usuario
from servidor import ServidorCorreo

# Crear servidor y usuarios
servidor = ServidorCorreo()
u1 = Usuario("Alice","alice@mail.com")
u2 = Usuario("Bob","bob@mail.com")
u3 = Usuario("Marquitos","marquitos@mail.com")

servidor.add_usuario(u1)
servidor.add_usuario(u2)
servidor.add_usuario(u3)

# Enviar mensajes
servidor.enviar_mensaje(u1, u2, "Hola", "¿Como estas?")
servidor.enviar_mensaje(u1, u2, "Chau", "Me voy...")
servidor.enviar_mensaje(u3, u2, "Volvi", "Giles")

# Revisar carpetas (devuelve listas)
entradas_u2 = u2.ver_entradas()
enviados_u1 = u1.ver_enviados()
enviados_u3 = u3.ver_enviados()

# Borrar usuario
servidor.delete_usuario(2)

# Ver nombres de usuarios existentes
usuarios_restantes = servidor.ver_usuariosnombres()

# Ejemplo de impresión si se desea mostrar
for msg in entradas_u2:
    print(msg)