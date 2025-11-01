from usuario import Usuario
from mensaje import Mensaje
from carpeta import Carpeta
from servidor import ServidorCorreo

# Servidores
servidor1 = ServidorCorreo("S1")
servidor2 = ServidorCorreo("S2")
servidor1.conectar_servidor(servidor2)

# Usuarios
u1 = Usuario("Alice","alice@mail.com")
u2 = Usuario("Bob","bob@mail.com")
u3 = Usuario("Marquitos","marquitos@mail.com")

servidor1.add_usuario(u1)
servidor1.add_usuario(u2)
servidor2.add_usuario(u3)

# Agregar filtros automáticos
u2.agregar_filtro({"asunto": "Urgente", "destino": "Proyectos"})
u2.agregar_filtro({"emisor": "Marquitos", "destino": "Personal"})

# Enviar mensajes
servidor1.enviar_mensaje(u1, u2, "Hola", "¿Cómo estás?", urgente=False)
servidor1.enviar_mensaje(u1, u2, "Urgente: Proyecto", "Revisar hoy", urgente=True)
servidor1.enviar_mensaje(u3, u2, "Volví", "Giles", urgente=True)

# Ver mensajes
print("Enviados por Alice:", u1.ver_enviados())
print("Entradas de Bob:", u2.ver_entradas())
print("Enviados por Marquitos:", u3.ver_enviados())

# Cola de prioridad
print("Mensajes urgentes en servidor1:")
for m in servidor1.cola_prioridad:
    print(m.imprimir_mensaje())

# Crear subcarpeta y mover mensaje manualmente
sub = Carpeta("Proyectos")
u2.get_carpeta()[0].add_subcarpeta(sub)
mensaje_a_mover = u2.get_carpeta()[0].get_mensajes()[0]
u2.get_carpeta()[0].mover_mensaje(mensaje_a_mover, sub)

# Búsqueda recursiva
encontrados = u2.get_carpeta()[0].buscar_mensajes(asunto="Hola")
for m in encontrados:
    print("Buscado:", m.imprimir_mensaje())