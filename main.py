from usuario import Usuario
from mensaje import Mensaje
from carpeta import Carpeta
from servidor import ServidorCorreo

# Crear servidores
servidor1 = ServidorCorreo("Servidor1")
servidor2 = ServidorCorreo("Servidor2")
servidor1.conectar_servidor(servidor2)

# Crear usuarios
alice = Usuario("Alice", "alice@mail.com")
bob = Usuario("Bob", "bob@mail.com")
marquitos = Usuario("Marquitos", "marquitos@mail.com")

# Asignar usuarios a servidores
servidor1.add_usuario(alice)
servidor1.add_usuario(bob)
servidor2.add_usuario(marquitos)

# Agregar filtros automáticos a Bob
bob.agregar_filtro({"asunto": "Urgente", "destino": "Proyectos"})
bob.agregar_filtro({"emisor": "Marquitos", "destino": "Personal"})

# Enviar mensajes
servidor1.enviar_mensaje(alice, bob, "Hola", "¿Cómo estás?", urgente=False)
servidor1.enviar_mensaje(alice, bob, "Urgente: Proyecto", "Revisar hoy", urgente=True)
servidor2.enviar_mensaje(marquitos, bob, "Volví", "Hola Bob!", urgente=True)

# Mostrar mensajes enviados por Alice
print("Mensajes enviados por Alice:")
for m in alice.ver_enviados():
    print(m)

# Mostrar mensajes de Bob
print("\nMensajes en bandeja de Bob:")
for m in bob.ver_entradas():
    print(m)

# Mostrar mensajes enviados por Marquitos
print("\nMensajes enviados por Marquitos:")
for m in marquitos.ver_enviados():
    print(m)

# Mostrar cola de urgentes del servidor1
print("\nMensajes urgentes en servidor1:")
for m in servidor1.cola_prioridad:
    print(m.imprimir_mensaje())

# Crear subcarpeta y mover un mensaje manualmente
proyectos = Carpeta("Proyectos")
entrada_bob = next(c for c in bob.get_carpeta() if c.get_cnombre() == "Entrada")
entrada_bob.add_subcarpeta(proyectos)
mensaje_a_mover = entrada_bob.get_mensajes()[0]
entrada_bob.mover_mensaje(mensaje_a_mover, proyectos)

# Búsqueda de mensajes por asunto
encontrados = entrada_bob.buscar_mensajes(asunto="Hola")
print("\nMensajes encontrados con asunto 'Hola':")
for m in encontrados:
    print(m.imprimir_mensaje())