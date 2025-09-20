Clases y Justificación del Diseño

Usuario

Responsabilidad: Mantener información del usuario y permitir acceder a sus carpetas y mensajes.

Decisiones de diseño:

Incluye nombre y correo como atributos.

Contiene una lista de Carpeta mediante composición (Entrada y Enviados).

Se agregan métodos ver_enviados y ver_entradas para acceder de forma controlada a los mensajes.

Métodos: set_unombre, set_correo, set_carpeta, get_unombre, get_correo, get_carpeta, ver_carpetas, ver_enviados, ver_entradas.

Mensaje

Responsabilidad: Representar un correo electrónico con toda su información.

Decisiones de diseño:

Contiene asunto, cuerpo, emisor y receptor.

Método crear_mensaje para inicializar de manera segura todos los atributos.

Método imprimir_mensaje para mostrar el mensaje, diferenciando entre enviados y entradas.

Métodos: set_asunto, set_cuerpo, set_emisor, set_receptor, get_asunto, get_cuerpo, get_emisor, get_receptor, crear_mensaje, imprimir_mensaje.

Carpeta

Responsabilidad: Gestionar un conjunto de mensajes.

Decisiones de diseño:

Atributos nombre y lista de mensajes.

Métodos para agregar y eliminar mensajes (add_mensaje, delete_mensaje).

Métodos para ver mensajes (ver_mensajes) e imprimirlos (imprimir_mensajes).

Métodos: set_cnombre, add_mensaje, delete_mensaje, get_cnombre, get_mensajes, ver_mensajes, imprimir_mensajes.

ServidorCorreo

Responsabilidad: Gestionar usuarios y el envío de mensajes.

Decisiones de diseño:

Contiene lista de usuarios.

Métodos add_usuario y delete_usuario para la administración de usuarios.

Método enviar_mensaje centraliza la creación del mensaje y su almacenamiento en las carpetas correspondientes.

Métodos: add_usuario, delete_usuario, get_usuarios, ver_usuariosnombres, enviar_mensaje.
