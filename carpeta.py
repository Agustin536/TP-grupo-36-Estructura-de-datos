# Carpeta
from mensaje import Mensaje

class Carpeta:
    def __init__(self, nombre=None):
        self.nombre = nombre
        self.mensajes = []

    def set_cnombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El parámetro debe ser un string")
        self.nombre = nombre

    def add_mensaje(self, mensaje):
        if not isinstance(mensaje, Mensaje):
            raise TypeError("Debe ser un objeto Mensaje")
        self.mensajes.append(mensaje)

    def delete_mensaje(self, i):
        if not isinstance(i, int):
            raise TypeError("Índice debe ser entero")
        if i < 0 or i >= len(self.mensajes):
            raise IndexError("Índice fuera de rango")
        self.mensajes.pop(i)

    def get_cnombre(self):
        return self.nombre

    def get_mensajes(self):
        return self.mensajes

    def ver_mensajes(self):
        return [m.get_asunto() for m in self.get_mensajes()]

    def listar_mensajes(self):
        # Devuelve la info completa de los mensajes como lista de tuplas
        return [m.info() for m in self.get_mensajes()]