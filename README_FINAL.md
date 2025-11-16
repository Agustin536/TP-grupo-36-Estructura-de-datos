# Cliente de Correo Electrónico - Proyecto Final ED Grupo 36

## Descripción
Sistema de gestión de correo electrónico implementado en Python que integra todas las funcionalidades desarrolladas en las entregas anteriores. Incluye:
- Gestión de usuarios.
- Envío y recepción de mensajes.
- Carpetas y subcarpetas recursivas.
- Filtros automáticos para mensajes entrantes.
- Mensajes urgentes con cola de prioridad.
- Red de servidores interconectados para envío distribuido de mensajes.
- Interfaz CLI y GUI simple para la interacción con el sistema.

## Integrantes del Grupo
- **Bruno Beer** - [brunojbeer@gmail.com] - Colaboración completa en todas las áreas.
- **Patricio Grano** - [granop13@gmail.com] - Colaboración completa en todas las áreas.
- **Agustin Ramos** - [agustinramos536@gmail.com] - Colaboración completa en todas las áreas.

> Todos los integrantes participaron en la implementación de clases, algoritmos y la interfaz de usuario.

## Tecnologías Utilizadas
- **Lenguaje:** Python 3.10+
- **Estructuras de Datos:**
  - Árboles generales (gestión de carpetas)
  - Colas de prioridad (mensajes urgentes)
  - Grafos (red de servidores)
- **Algoritmos:**
  - Recursividad (búsquedas en árbol de carpetas)
  - BFS/DFS (enrutamiento de mensajes entre servidores)
- **Testing:** pytest
- **Control de Versiones:** Git/GitHub

## Características Principales
### ✉ Gestión de Mensajes
- Envío y recepción de mensajes
- Mensajes con prioridad "urgente"
- Etiquetado y categorización con filtros automáticos
- Búsqueda avanzada por asunto o remitente

### 📁 Sistema de Carpetas
- Estructura jerárquica de carpetas (árbol general)
- Subcarpetas ilimitadas
- Búsqueda recursiva de mensajes
- Movimiento de mensajes entre carpetas

### 🔍 Filtros Automáticos
- Creación de reglas de filtrado
- Aplicación automática a mensajes entrantes
- Múltiples criterios: remitente, asunto

### 🚀 Mensajes Urgentes
- Cola de prioridades para mensajes importantes
- Procesamiento preferencial en la interfaz

### 🌐 Red de Servidores
- Grafo de servidores interconectados
- Enrutamiento inteligente con BFS/DFS
- Simulación de envío de mensajes entre dominios

## Instalación

### Requisitos Previos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/Agustin536/TP-grupo-36-Estructura-de-datos
cd TP-grupo-36-Estructura-de-datos
```
2. Crear entorno virtual: 
```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
3. Instalar dependencias:
```
pip install -r requirements.txt
```
4. Verificar instalación:
```
python -m pytest tests/
```

### Uso
#### Ejecución del Sistema
```bash
python main.py
python -m pytest tests/
```
### Interfaz de Línea de Comandos

El sistema presenta un menú interactivo como este:
```
=== CLIENTE DE CORREO ELECTRÓNICO ===
```
1. Enviar Mensaje
2. Ver Bandeja de Entrada
3. Gestionar Carpetas
4. Configurar Filtros
5. Ver Mensajes Urgentes
6. Administrar Red de Servidores
0. Salir
Seleccione una opción:

## Estructura del Proyecto
cliente_correo/
├── main.py # Archivo principal de ejecución
├── usuario.py # Clase Usuario y filtros automáticos
├── mensaje.py # Clase Mensaje
├── carpeta.py # Clase Carpeta
├── servidor.py # Clase ServidorCorreo y manejo de red
├── interfaces.py # Interfaces de Mensajes
├── cli.py # Interfaz de línea de comandos
├── gui_tk.py # Interfaz gráfica con Tkinter
└── README.md # Documentación del proyecto
