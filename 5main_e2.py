# Pruebas
servidor = ServidorCorreo()
u1 = Usuario("Alice", "alice@mail.com")
u2 = Usuario("Bob", "bob@mail.com")
u3 = Usuario("Marquitos", "marquitos@mail.com")

servidor.add_usuario(u1)
servidor.add_usuario(u2)
servidor.add_usuario(u3)

servidor.enviar_mensaje(u1, u2, "Hola", "¿Cómo estás?")
servidor.enviar_mensaje(u1, u2, "Chau", "Me voy...")
servidor.enviar_mensaje(u3, u2, "Volví", "Giles")

# Ver mensajes
print(u1.ver_enviados())
print(u2.ver_entradas())
print(u3.ver_enviados())

# Crear subcarpeta y mover mensaje
sub = Carpeta("Proyectos")
u2.get_carpeta()[0].add_subcarpeta(sub)
mensaje_a_mover = u2.get_carpeta()[0].get_mensajes()[0]
u2.get_carpeta()[0].mover_mensaje(mensaje_a_mover, sub)

# Buscar mensaje recursivo
encontrados = u2.get_carpeta()[0