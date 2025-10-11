# Clase ServidorCorreo
class ServidorCorreo(IEnviarMensaje):
    def __init__(self):
        self.usuarios = []

    def add_usuario(self, usuario):
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

    def enviar_mensaje(self, usuario_emisor, usuario_receptor, asunto, cuerpo):
        if not isinstance(usuario_emisor, Usuario) or not isinstance(usuario_receptor, Usuario):
            raise TypeError("Emisor y receptor deben ser Usuario")

        emisor = next((c for c in self.usuarios if c.get_correo() == usuario_emisor.get_correo()), None)
        receptor = next((c for c in self.usuarios if c.get_correo() == usuario_receptor.get_correo()), None)

        if not emisor or not receptor:
            raise ValueError("Emisor o receptor no encontrado")

        mensaje = Mensaje()
        mensaje.crear_mensaje(asunto, cuerpo, usuario_emisor, usuario_receptor)

        enviados = next((c for c in usuario_emisor.get_carpeta() if c.get_cnombre() == "Enviados"), None)
        entrada = next((c for c in usuario_receptor.get_carpeta() if c.get_cnombre() == "Entrada"), None)

        enviados.add_mensaje(mensaje)
        entrada.add_mensaje(mensaje)