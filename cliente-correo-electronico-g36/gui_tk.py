import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from servidor import ServidorCorreo
from usuario import Usuario

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Correo - GUI")
        self.servidor = ServidorCorreo("Servidor GUI")

        frm = tk.Frame(root, padx=10, pady=10)
        frm.pack()

        tk.Label(frm, text="Nombre").grid(row=0, column=0, sticky="w")
        self.entry_nombre = tk.Entry(frm, width=30)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(frm, text="Correo").grid(row=1, column=0, sticky="w")
        self.entry_correo = tk.Entry(frm, width=30)
        self.entry_correo.grid(row=1, column=1)

        tk.Button(frm, text="Crear Usuario", command=self.crear_usuario).grid(row=2, column=0, columnspan=2, pady=(5,10))

        tk.Button(frm, text="Enviar Mensaje", command=self.ventana_enviar).grid(row=3, column=0, columnspan=2, sticky="we")
        tk.Button(frm, text="Ver Bandeja", command=self.ventana_ver_bandeja).grid(row=4, column=0, columnspan=2, sticky="we")
        tk.Button(frm, text="Listar Usuarios", command=self.listar_usuarios).grid(row=5, column=0, columnspan=2, sticky="we")

    def crear_usuario(self):
        nombre = self.entry_nombre.get().strip()
        correo = self.entry_correo.get().strip()
        if not nombre or not correo:
            messagebox.showwarning("Aviso", "Nombre y correo requeridos")
            return
        u = Usuario(nombre, correo)
        self.servidor.add_usuario(u)
        messagebox.showinfo("OK", f"Usuario {nombre} creado")

    def listar_usuarios(self):
        usuarios = self.servidor.get_usuarios()
        if not usuarios:
            messagebox.showinfo("Usuarios", "No hay usuarios")
            return
        texto = "\n".join([f"{u.get_unombre()} <{u.get_correo()}>" for u in usuarios])
        messagebox.showinfo("Usuarios", texto)

    def ventana_enviar(self):
        Em = simpledialog.askstring("Enviar", "Correo emisor:")
        Rc = simpledialog.askstring("Enviar", "Correo receptor:")
        if not Em or not Rc:
            return
        asunto = simpledialog.askstring("Enviar", "Asunto:")
        cuerpo = simpledialog.askstring("Enviar", "Cuerpo:")
        urgente = messagebox.askyesno("Urgente", "Marcar como urgente?")
        em = next((u for u in self.servidor.get_usuarios() if u.get_correo() == Em), None)
        rc = next((u for u in self.servidor.get_usuarios() if u.get_correo() == Rc), None)
        if em is None or rc is None:
            messagebox.showerror("Error", "Emisor o receptor no encontrados")
            return
        self.servidor.enviar_mensaje(em, rc, asunto or "", cuerpo or "", urgente)
        messagebox.showinfo("OK", "Mensaje enviado")

    def ventana_ver_bandeja(self):
        correo = simpledialog.askstring("Ver bandeja", "Correo del usuario:")
        if not correo:
            return
        u = next((u for u in self.servidor.get_usuarios() if u.get_correo() == correo), None)
        if u is None:
            messagebox.showerror("Error", "Usuario no encontrado")
            return
        entradas = u.ver_entradas() or []
        win = tk.Toplevel(self.root)
        win.title(f"Bandeja de {correo}")
        txt = scrolledtext.ScrolledText(win, width=80, height=20)
        txt.pack(padx=10, pady=10)
        if not entradas:
            txt.insert("end", "Bandeja vacía\n")
        else:
            for i, m in enumerate(entradas, start=1):
                txt.insert("end", f"--- Mensaje {i} ---\n")
                txt.insert("end", f"Asunto: {m['asunto']}\n")
                txt.insert("end", f"De: {m['emisor']}\n")
                txt.insert("end", f"Para: {m['receptor']}\n")
                txt.insert("end", f"Urgente: {m['urgente']}\n")
                txt.insert("end", f"Cuerpo: {m['cuerpo']}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
