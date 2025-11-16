from servidor import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje
import sys

def buscar_usuario_por_correo(servidor, correo):
    for u in servidor.get_usuarios():
        if u.get_correo() == correo:
            return u
    return None

def crear_usuario_interactivo(servidor):
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    if not nombre or not correo:
        print("Nombre y correo requeridos.")
        return
    u = Usuario(nombre, correo)
    servidor.add_usuario(u)
    print(f"Usuario '{nombre}' creado.")

def listar_usuarios(servidor):
    if not servidor.get_usuarios():
        print("No hay usuarios registrados.")
        return
    for i, u in enumerate(servidor.get_usuarios()):
        print(f"{i+1}. {u.get_unombre()} <{u.get_correo()}>")

def enviar_mensaje_interactivo(servidor):
    em_correo = input("Correo emisor: ").strip()
    rc_correo = input("Correo receptor: ").strip()
    asunto = input("Asunto: ").strip()
    cuerpo = input("Cuerpo: ").strip()
    urgente_in = input("Urgente? (s/n): ").lower().strip()
    urgente = urgente_in == "s"

    em = buscar_usuario_por_correo(servidor, em_correo)
    rc = buscar_usuario_por_correo(servidor, rc_correo)
    if em is None:
        print("Emisor no encontrado.")
        return
    if rc is None:
        print("Receptor no encontrado.")
        return

    servidor.enviar_mensaje(em, rc, asunto, cuerpo, urgente)
    print("Mensaje enviado.")

def ver_bandeja(servidor):
    correo = input("Correo del usuario: ").strip()
    u = buscar_usuario_por_correo(servidor, correo)
    if u is None:
        print("Usuario no encontrado.")
        return
    entradas = u.ver_entradas()
    if not entradas:
        print("Bandeja vacía.")
        return
    for i, m in enumerate(entradas, 1):
        print(f"\n--- Mensaje {i} ---")
        print(f"Asunto: {m['asunto']}")
        print(f"De: {m['emisor']}")
        print(f"Para: {m['receptor']}")
        print(f"Urgente: {m['urgente']}")
        print(f"Cuerpo: {m['cuerpo']}")

def procesar_cola_urgentes(servidor):
    from collections import deque
    if not hasattr(servidor, "cola_prioridad") or not servidor.cola_prioridad:
        print("No hay mensajes urgentes.")
        return
    print("Procesando cola de urgentes:")
    while servidor.cola_prioridad:
        m = servidor.cola_prioridad.popleft()
        print(f"- {m.get_asunto()} (de {m.get_emisor().get_unombre()} a {m.get_receptor().get_unombre()})")

def main():
    servidor = ServidorCorreo("Servidor Local")
    print("=== CLI - Sistema de Correo ===")
    while True:
        print("\nOpciones:")
        print("1) Crear usuario")
        print("2) Listar usuarios")
        print("3) Enviar mensaje")
        print("4) Ver bandeja de entrada")
        print("5) Procesar cola de urgentes")
        print("6) Salir")
        op = input("Elegí una opción: ").strip()
        if op == "1":
            crear_usuario_interactivo(servidor)
        elif op == "2":
            listar_usuarios(servidor)
        elif op == "3":
            enviar_mensaje_interactivo(servidor)
        elif op == "4":
            ver_bandeja(servidor)
        elif op == "5":
            procesar_cola_urgentes(servidor)
        elif op == "6":
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
