# Clase Usuario 
class Usuario(IRecibirMensaje, IListarMensajes):
    def __init__(self, nombre=None, correo=None):
        self.nombre = nombre
        self.correo = correo
        self.carpeta = [Carpeta("Entrada"), Carpeta("Enviados")]

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