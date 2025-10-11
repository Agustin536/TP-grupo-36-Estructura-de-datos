# Clase Carpeta (Arbol general con subcarpetas)
class Carpeta:
    def __init__(self, nombre=None):
        self.nombre = nombre
        self.mensajes = []
        self.subcarpetas = []

    def set_cnombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("Debe ser un string")
        self.nombre = nombre

    def add_mensaje(self, mensaje):
        if not isinstance(mensaje, Mensaje):
            raise TypeError("Debe ser un Mensaje")
        self.mensajes.append(mensaje)

    def delete_mensaje(self, mensaje):
        if mensaje in self.mensajes:
            self.mensajes.remove(mensaje)
        else:
            for sub in self.subcarpetas:
                sub.delete_mensaje(mensaje)

    def add_subcarpeta(self, carpeta):
        if not isinstance(carpeta, Carpeta):
            raise TypeError("Debe ser una Carpeta")
        self.subcarpetas.append(carpeta)

    def get_cnombre(self):
        return self.nombre

    def get_mensajes(self):
        return self.mensajes

    def ver_mensajes(self):
        return [m.get_asunto() for m in self.mensajes]

    def imprimir_mensajes(self):
        resultados = []
        for m in self.mensajes:
            resultados.append(m.imprimir_mensaje())
        for sub in self.subcarpetas:
            resultados.extend(sub.imprimir_mensajes())
        return resultados

    # Busqueda recursiva
    def buscar_mensajes(self, asunto=None, emisor=None):
        encontrados = []
        for m in self.mensajes:
            if (asunto and m.get_asunto() == asunto) or (emisor and m.get_emisor() == emisor):
                encontrados.append(m)
        for sub in self.subcarpetas:
            encontrados.extend(sub.buscar_mensajes(asunto, emisor))
        return encontrados

    # Mover mensaje
    def mover_mensaje(self, mensaje, carpeta_destino):
        if mensaje in self.mensajes:
            self.mensajes.remove(mensaje)
            carpeta_destino.add_mensaje(mensaje)
        else:
            for sub in self.subcarpetas:
                sub.mover_mensaje(mensaje, carpeta_destino)
