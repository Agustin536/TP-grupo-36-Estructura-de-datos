# Usuario
from carpeta import Carpeta
from abc import ABC, abstractmethod

# Interfaces que implementa Usuario
class IRecibirMensaje(ABC):
    @abstractmethod
    def ver_entradas(self):
        pass

class IListarMensajes(ABC):
    @abstractmethod
    def ver_enviados(self):
        pass

class Usuario(IRecibirMensaje, IListarMensajes):
    def __init__(self, nombre=None, correo=None):
        self.nombre = nombre
        self.correo = correo
        self.carpeta = [Carpeta(), Carpeta()]
        self.carpeta[0].set_cnombre("Entrada")
        self.carpeta[1].set_cnombre("Enviados")

    def set_unombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El parámetro debe ser un string")
        self.nombre = nombre

    def set_correo(self, correo):
        if not isinstance(correo, str):
            raise TypeError("El parámetro debe ser un string")
        self.correo = correo

    def set_carpeta(self, carpeta):
        if not isinstance(carpeta, Carpeta):
            raise TypeError("El parámetro debe ser un objeto de la clase Carpeta")
        self.carpeta.append(carpeta)

    def get_unombre(self):
        return self.nombre

    def get_correo(self):
        return self.correo

    def get_carpeta(self):
        return self.carpeta

    def ver_carpetas(self):
        return [folder.get_cnombre() for folder in self.carpeta]

    def ver_enviados(self):
        enviados = self.get_carpeta()[1]
        return enviados.listar_mensajes()

    def ver_entradas(self):
        entradas = self.get_carpeta()[0]
        return entradas.listar_mensajes()