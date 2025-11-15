from abc import ABC, abstractmethod
from usuario import Usuario
from carpeta import Carpeta
from mensaje import Mensaje
from collections import deque

# Interfaz
class IEnviarMensaje(ABC):
    @abstractmethod
    def enviar_mensaje(self, usuario_emisor, usuario_receptor, asunto, cuerpo, urgente=False):
        pass

# Clase ServidorCorreo
class ServidorCorreo(IEnviarMensaje):
    def __init__(self, nombre="Servidor"):
        self.nombre = nombre
        self.usuarios = []
        self.conexiones = []  # lista de otros servidores (grafo)
        self.cola_prioridad = deque()  # mensajes urgentes

    def add_usuario(self, usuario: Usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("Debe ser un Usuario")
        self.usuarios.append(usuario)

    def delete_usuario(self, i):
        if not isinstance(i, int):
            raise TypeError("Debe ser un entero")
        if i < 0 or i >= len(self.usuarios):
            raise IndexError("Índice fuera de rango")
        self.usuarios.pop(i)

    def get_usuarios(self):
        return self.usuarios

    def ver_usuariosnombres(self):
        return [u.get_unombre() for u in self.usuarios]

    def enviar_mensaje(self, usuario_emisor, usuario_receptor, asunto, cuerpo, urgente=False):
        if not isinstance(usuario_emisor, Usuario) or not isinstance(usuario_receptor, Usuario):
            raise TypeError("Emisor y receptor deben ser Usuario")

        mensaje = Mensaje()
        mensaje.crear_mensaje(asunto, cuerpo, usuario_emisor, usuario_receptor, urgente)

        # Manejo de carpetas
        enviados = next((c for c in usuario_emisor.get_carpeta() if c.get_cnombre() == "Enviados"), None)
        entrada = next((c for c in usuario_receptor.get_carpeta() if c.get_cnombre() == "Entrada"), None)

        enviados.add_mensaje(mensaje)
        entrada.add_mensaje(mensaje)

        # Aplicar filtros automáticos
        usuario_receptor.aplicar_filtros(mensaje)

        if urgente:
            self.cola_prioridad.append(mensaje)

    # Grafo de servidores
    def conectar_servidor(self, otro_servidor):
        if otro_servidor not in self.conexiones:
            self.conexiones.append(otro_servidor)
            otro_servidor.conectar_servidor(self)

    def enviar_a_servidores(self, mensaje: Mensaje):
        visitados = set()
        queue = deque([self])
        while queue:
            servidor_actual = queue.popleft()
            if servidor_actual in visitados:
                continue
            visitados.add(servidor_actual)
            for u in servidor_actual.usuarios:
                if u.get_correo() == mensaje.get_receptor().get_correo():
                    entrada = next((c for c in u.get_carpeta() if c.get_cnombre() == "Entrada"), None)
                    entrada.add_mensaje(mensaje)
                    u.aplicar_filtros(mensaje)
            for vecino in servidor_actual.conexiones:
                if vecino not in visitados:
                    queue.append(vecino)