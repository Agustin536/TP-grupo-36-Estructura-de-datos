# Mensaje
from usuario import Usuario

class Mensaje:
    def __init__(self, asunto=None, cuerpo=None, emisor=None, receptor=None):
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.emisor = emisor
        self.receptor = receptor

    def set_asunto(self, asunto):
        if not isinstance(asunto, str):
            raise TypeError("El parámetro debe ser un string")
        self.asunto = asunto

    def set_cuerpo(self, cuerpo):
        if not isinstance(cuerpo, str):
            raise TypeError("El parámetro debe ser un string")
        self.cuerpo = cuerpo

    def set_emisor(self, emisor):
        if not isinstance(emisor, Usuario):
            raise TypeError("El parámetro debe ser un Usuario")
        self.emisor = emisor

    def set_receptor(self, receptor):
        if not isinstance(receptor, Usuario):
            raise TypeError("El parámetro debe ser un Usuario")
        self.receptor = receptor

    def get_asunto(self):
        return self.asunto

    def get_cuerpo(self):
        return self.cuerpo

    def get_emisor(self):
        return self.emisor

    def get_receptor(self):
        return self.receptor

    def crear_mensaje(self, asunto=None, cuerpo=None, emisor=None, receptor=None):
        if asunto: self.set_asunto(asunto)
        if cuerpo: self.set_cuerpo(cuerpo)
        if emisor: self.set_emisor(emisor)
        if receptor: self.set_receptor(receptor)

    def info(self):
        # Devuelve la informacion del mensaje como tupla
        return (self.asunto, self.cuerpo, self.emisor.get_unombre(), self.receptor.get_unombre())