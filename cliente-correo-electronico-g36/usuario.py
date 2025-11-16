from abc import ABC, abstractmethod
from carpeta import Carpeta

# Interfaces
class IRecibirMensaje(ABC):
    @abstractmethod
    def ver_entradas(self):
        pass

class IListarMensajes(ABC):
    @abstractmethod
    def ver_enviados(self):
        pass

# Clase Usuario
class Usuario(IRecibirMensaje, IListarMensajes):
    def __init__(self, nombre=None, correo=None):
        self.nombre = nombre
        self.correo = correo
        self.carpeta = [Carpeta("Entrada"), Carpeta("Enviados")]
        self.filtros = []  # Lista de filtros automáticos

    def set_unombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("Debe ser un string")
        self.nombre = nombre

    def set_correo(self, correo):
        if not isinstance(correo, str):
            raise TypeError("Debe ser un string")
        self.correo = correo

    def set_carpeta(self, carpeta):
        if not isinstance(carpeta, Carpeta):
            raise TypeError("Debe ser una Carpeta")
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
        enviados = next((c for c in self.carpeta if c.get_cnombre() == "Enviados"), None)
        if enviados:
            return enviados.imprimir_mensajes()

    def ver_entradas(self):
        entradas = next((c for c in self.carpeta if c.get_cnombre() == "Entrada"), None)
        if entradas:
            return entradas.imprimir_mensajes()

    # Filtros automáticos
    def agregar_filtro(self, criterio: dict):
        """
        Ejemplo de criterio: {"asunto": "Urgente", "destino": "Proyectos"}
        """
        if not isinstance(criterio, dict):
            raise TypeError("El filtro debe ser un diccionario")
        self.filtros.append(criterio)

    def aplicar_filtros(self, mensaje):
        """
        Aplica todos los filtros definidos al mensaje recibido
        """
        from mensaje import Mensaje
        if not isinstance(mensaje, Mensaje):
            raise TypeError("Debe ser una Carpeta")
        for filtro in self.filtros:
            destino_nombre = filtro.get("destino")
            if not destino_nombre:
                continue
            destino_carpeta = next((c for c in self.carpeta if c.get_cnombre() == destino_nombre), None)
            if not destino_carpeta:
                # Crear subcarpeta si no existe
                destino_carpeta = Carpeta(destino_nombre)
                self.carpeta.append(destino_carpeta)

            # Verificar criterio
            cumple = True
            for clave, valor in filtro.items():
                if clave == "asunto" and valor not in mensaje.get_asunto():
                    cumple = False
                if clave == "emisor" and valor != mensaje.get_emisor().get_unombre():
                    cumple = False
            if cumple:
                destino_carpeta.add_mensaje(mensaje)
                # También eliminar de Entrada si ya estaba agregado ahí
                entrada = next((c for c in self.carpeta if c.get_cnombre() == "Entrada"), None)
                if entrada and mensaje in entrada.get_mensajes():
                    entrada.delete_mensaje(mensaje)