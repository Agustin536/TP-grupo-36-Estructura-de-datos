# Servidor
from usuario import Usuario
from mensaje import Mensaje
from abc import ABC, abstractmethod

class IEnviarMensaje(ABC):
    @abstractmethod
    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):
        pass

class ServidorCorreo(IEnviarMensaje):
    def __init__(self):
        self.usuarios = []

    def add_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("Debe ser un Usuario")
        self.usuarios.append(usuario)

    def delete_usuario(self, i):
        if not isinstance(i, int):
            raise TypeError("Índice debe ser entero")
        if i < 0 or i >= len(self.usuarios):
            raise IndexError("Índice fuera de rango")
        self.usuarios.pop(i)

    def get_usuarios(self):
        return self.usuarios

    def ver_usuariosnombres(self):
        return [u.get_unombre() for u in self.get_usuarios()]

    def enviar_mensaje(self, usuario_emisor, usuario_receptor, asunto, cuerpo):
        if not isinstance(usuario_emisor, Usuario) or not isinstance(usuario_receptor, Usuario):
            raise TypeError("Emisor y receptor deben ser instancias de Usuario")

        emisor = next((u for u in self.get_usuarios() if u.get_correo() == usuario_emisor.get_correo()), None)
        receptor = next((u for u in self.get_usuarios() if u.get_correo() == usuario_receptor.get_correo()), None)
        if not emisor or not receptor:
            raise ValueError("Emisor o receptor no encontrado")

        mensaje = Mensaje()
        mensaje.crear_mensaje(asunto=asunto, cuerpo=cuerpo, emisor=usuario_emisor, receptor=usuario_receptor)

        enviados = next((c for c in usuario_emisor.get_carpeta() if c.get_cnombre() == "Enviados"), None)
        entradas = next((c for c in usuario_receptor.get_carpeta() if c.get_cnombre() == "Entrada"), None)
        if not enviados or not entradas:
            raise ValueError("Faltan carpetas necesarias")

        enviados.add_mensaje(mensaje)
        entradas.add_mensaje(mensaje)