"""
Clase Usuario
"""

class Usuario:
  '''
  summary: vamos a hacer una clase usuario que se inicialice con sus atributos en None, que luego tenga métodos de set para poder ingresar sus datos
  y sus respectivos get para poder obtenerlos (a excepción de la clave por obvias razones).
  '''

  #Constructor
  def __init__(self, nombre = None, correo = None):
    self.nombre = nombre
    self.correo = correo
    self.carpeta = [Carpeta(), Carpeta()]
    self.carpeta[0].set_cnombre("Entrada")
    self.carpeta[1].set_cnombre("Enviados")

  #Funciones de set

  #nombre
  def set_unombre(self, nombre):
    try:
      if not isinstance(nombre, str):
        raise TypeError("El parámetro debe ser un string")
      else:
        self.nombre = nombre
    except TypeError:
      raise

  #correo
  def set_correo(self, correo):
    try:
      if not isinstance(correo, str):
        raise TypeError("El parámetro debe ser un string")
      else:
        self.correo = correo
    except TypeError:
      raise

  #carpeta
  def set_carpeta(self, carpeta):
    try:
      if not isinstance(carpeta, Carpeta):
        raise TypeError("El parámetro debe ser un objeto de la clase Carpeta")
      else:
        self.carpeta.append(carpeta)
    except TypeError:
      raise

  #Funciones de get
  def get_unombre(self):
    return self.nombre

  def get_correo(self):
    return self.correo

  def get_carpeta(self):
    return self.carpeta

  #Ver nombres de las carpetas
  def ver_carpetas(self):
    aux = []
    for folder in self.carpeta:
      aux.append(folder.get_nombre())
    return aux

  #Ver todo el contenido de los mensajes enviados en la carpeta Enviados
  def ver_enviados(self):
    env = self.carpeta[1] #indice 1 es Enviados
    env.imprimir_mensajes("env")

  #Ver todo el contenido de los mensajes entrantes en la carpeta Entradas
  def ver_entradas(self):
    ent = self.carpeta[0] #indice 0 es Entradas
    ent.imprimir_mensajes("ent")

"""Clase Mensaje"""

class Mensaje:

  def __init__(self, asunto = None, cuerpo = None, emisor = None, receptor = None):
    self.asunto = asunto
    self.cuerpo = cuerpo
    self.emisor = emisor
    self.receptor = receptor

  #Funciones de set individuales

  #Asunto
  def set_asunto(self, asunto):
    try:
      if not isinstance(asunto, str):
        raise TypeError("El parámetro debe ser un string")
      else:
        self.asunto = asunto
    except TypeError:
      raise
  #Cuerpo
  def set_cuerpo(self, cuerpo):
    try:
      if not isinstance(cuerpo, str):
        raise TypeError("El parámetro debe ser un string")
      else:
        self.cuerpo = cuerpo
    except TypeError:
      raise
  #Emisor
  def set_emisor(self, emisor):
    try:
      if not isinstance(emisor, Usuario):
        raise TypeError("El parámetro debe ser un objeto de la clase Usuario")
      else:
        self.emisor = emisor
    except TypeError:
      raise
  #Receptor
  def set_receptor(self, receptor):
    try:
      if not isinstance(receptor, Usuario):
        raise TypeError("El parámetro debe ser un objeto de la clase Usuario")
      else:
        self.receptor = receptor
    except TypeError:
      raise

  #Funciones de get
  def get_asunto(self):
    return self.asunto

  def get_cuerpo(self):
    return self.cuerpo

  def get_emisor(self):
    return self.emisor

  def get_receptor(self):
    return self.receptor

  #Métodos generales
  def crear_mensaje(self, asunto=None, cuerpo=None, emisor=None, receptor=None): #Mover a clase Usuario?
    if not asunto:
      print("- Asunto no definido.")
    else:
      self.set_asunto(asunto)

    if not cuerpo:
      print("- Cuerpo no definido.")
    else:
      self.set_cuerpo(cuerpo)

    if not emisor:
      print("- Emisor no definido.")
    else:
      self.set_emisor(emisor)

    if not receptor:
      print("- Receptor no definido.")
    else:
      self.set_receptor(receptor)

  #Imprimir mensaje entero
  def imprimir_mensaje(self, origen = None):
    if origen == "ent":
      print(f"Carpeta Entrada de {self.receptor.get_unombre()}:")
    elif origen == "env":
      print(f"Carpeta Enviados de {self.emisor.get_unombre()}:")

    print(f"Asunto: {self.get_asunto()}")
    print(f"Cuerpo: {self.get_cuerpo()}")
    print(f"Emisor: {self.get_emisor().get_unombre()}\n")

"""Clase Carpeta"""

class Carpeta:

  def __init__(self, nombre = None):
    self.nombre = nombre
    self.mensajes = []


  def set_cnombre(self, nombre):
    try:
      if not isinstance(nombre, str):
        raise TypeError("El parámetro debe ser un string")
      else:
        self.nombre = nombre
    except TypeError:
      raise

  def add_mensaje(self, mensaje):
    try:
      if not isinstance(mensaje, Mensaje):
        raise TypeError("El parámetro debe ser un objeto de la clase Mensaje")
      else:
        self.mensajes.append(mensaje)
    except TypeError:
      raise

  def delete_mensaje(self, i):
    if not isinstance(i, int):
        raise TypeError("El parámetro debe ser un entero")

    if i < 0 or i >= len(self.mensajes):
        raise IndexError("El índice está fuera de rango")

    self.mensajes.pop(i)

  def get_cnombre(self):
    return self.nombre

  def ver_mensajes(self):
    aux = []
    for mensaje in self.mensajes:
      aux.append(mensaje.get_asunto())
      #print(aux)
    return aux

  def imprimir_mensajes(self, origen = None):
    for mensaje in self.mensajes:
      mensaje.imprimir_mensaje(origen)

"""Clase ServidorCorreo"""

class ServidorCorreo:

  def __init__(self):
    self.usuarios = []

  def add_usuario(self, usuario):
    try:
      if not isinstance(usuario, Usuario):
        raise TypeError("El parámetro debe ser un objeto de la clase Usuario")
      else:
        self.usuarios.append(usuario)
    except TypeError:
      raise

  def enviar_mensaje(self,usuario_emisor, usuario_receptor, asunto, cuerpo):
    if not isinstance(usuario_emisor, Usuario) or not isinstance(usuario_receptor, Usuario):
      raise TypeError("Emisor y receptor deben ser instancias de Usuario")

    # crear mensaje
    mensaje = Mensaje()
    mensaje.crear_mensaje(asunto=asunto, cuerpo=cuerpo, emisor=usuario_emisor, receptor=usuario_receptor)

    # buscar carpetas "Enviados" y "Entrada"
    enviados = next((c for c in usuario_emisor.get_carpeta() if c.get_cnombre() == "Enviados"), None)
    entrada = next((c for c in usuario_receptor.get_carpeta() if c.get_cnombre() == "Entrada"), None)

    if enviados is None or entrada is None:
      raise ValueError("Faltan carpetas necesarias en alguno de los usuarios")

    # guardar mensaje en ambas carpetas
    enviados.add_mensaje(mensaje)
    entrada.add_mensaje(mensaje)

"""Pruebas"""

# Crear servidor y usuarios
servidor = ServidorCorreo()
#u1 = Usuario(); u1.set_unombre("Alice"); u1.set_correo("alice@mail.com")
#u2 = Usuario(); u2.set_unombre("Bob");   u2.set_correo("bob@mail.com")
#u3 = Usuario(); u3.set_unombre("Marquitos");   u3.set_correo("bob@mail.com")
u1 = Usuario("Alice","alice@mail.com")
u2 = Usuario("Bob","bob@mail.com")
u3 = Usuario("Marquitos","bob@mail.com")

servidor.add_usuario(u1)
servidor.add_usuario(u2)


# Enviar mensaje
servidor.enviar_mensaje(u1, u2, "Hola", "¿Cómo estás?")
servidor.enviar_mensaje(u1, u2, "Chau", "Me voy...")
servidor.enviar_mensaje(u3, u2, "Volvi", "Giles")

# Revisar carpetas
print("Carpeta Enviados de Alice:", u1.get_carpeta()[1].ver_mensajes()) #ver_enviados
print("Carpeta Entrada de Bob:", u2.get_carpeta()[0].ver_mensajes()) #ver_entradas

u2.ver_entradas()

u1.ver_enviados()
u2.ver_entradas()
u3.ver_enviados()
