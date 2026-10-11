import customtkinter as ctk # Esta es la libreria que estoy usando para diseñar y crear pantallas
# Estas librerias son mas orientadas a POO por eso se crean clases y métodos
from componentes import mostrar_alerta        
from conexion import base_datos as BaseDeDatos
from registro import RegistroWindow            

class LoginWindow(ctk.CTk):
    def __init__ (self):
        super().__init__()# Aqui se inicializa la pantalla en el constructor de la clase
        self.db = BaseDeDatos()
        # Leo esta es la configuracion de la ventana principal 
        self.title("FAZBEAR ENTERTAINMENT - SECURITY LOGIN") # Titulo de la pantalla
        self.geometry("750x450") # Tamaño de la pantalla
        self.resizable(False, False)
 
        # Configuracion de diseño
        ctk.set_appearance_mode("Dark")
        self.configure(fg_color="#000000") # COLOR DEL FONDO DE LA PANTALLA

        self.configurar_elementos() # Cargo todos los elementos en la pantalla principal

    def configurar_elementos(self):
        # Aqui vamos a ir poniendo todos los elemnetos como cajas de texto y asi 
        self.lbl_titulo = ctk.CTkLabel(
            self, # Con eso estoy diciendo que se van a pintar en la pantalla principal y siempre se recibe como primer argumento
            text="Five Nights at Freddy's",
            font=("Courier New", 26, "bold"),
            text_color="#FFFFFF",
        )
        self.lbl_titulo.place(x=60, y=110) # Aqui los pongo en la posicion que yo quiera en la pantalla

        self.lbl_subtitulo = ctk.CTkLabel(
            self,
            text="SECURYTY SYSTEM v1.0",
            font=("Courier New", 10, "bold"),
            text_color="#FF1E3B",
        )
        self.lbl_subtitulo.place(x=60, y=160)

        self.lbl_bienvenido = ctk.CTkLabel(
            self,
            text="Welcome!",
            font=("Courier New", 20, "bold"),
            text_color="#FFFFFF",
        )
        self.lbl_bienvenido.place(x=350, y=160)

        self.lbl_usuario = ctk.CTkLabel(
            self,
            text="Username",
            font=("Courier New", 12, "bold"),
            text_color="#FF1E3B",
        )
        self.lbl_usuario.place(x=350, y=200)

        self.entry_usuario = ctk.CTkEntry(
            self,
            width=260, 
            height=35,
            fg_color="#1A1A1A",
            border_color="#333333", 
            text_color="#FFFFFF",
            font=("Courier New", 12, "bold")
        )
        self.entry_usuario.place(x=420, y=200)

        self.lbl_contraseña = ctk.CTkLabel(
            self,
            text="Password",
            font=("Courier New", 12, "bold"),
            text_color="#FF1E3B",
        )
        self.lbl_contraseña.place(x=350, y=245)

        self.entry_contraseña = ctk.CTkEntry(
            self,
            width=260, 
            height=35,
            fg_color="#1A1A1A",
            border_color="#333333", 
            text_color="#FFFFFF",
            font=("Courier New", 12, "bold"),
            show = "*"
        )
        self.entry_contraseña.place(x=420, y=245)

        self.btn_login = ctk.CTkButton(
            self,
            text = "SIGN IN",
            width=120, 
            height=30,
            fg_color="#1A1A1A", 
            hover_color="#333333",
            text_color="#FFFFFF",
            font=("Courier New", 14, "bold"),
            border_color="#555555",
            border_width=1,
            command=self.validar_cajas
        )
        self.btn_login.place(x=555, y= 300)

        self.btn_registrar = ctk.CTkButton(
            self,
            text = "SIGN UP",
            width=120, 
            height=30,
            fg_color="#1A1A1A", 
            hover_color="#333333",
            text_color="#FFFFFF",
            font=("Courier New", 14, "bold"),
            border_color="#555555",
            border_width=1,
            command = self.abrir_registro
        )
        self.btn_registrar.place(x=420, y= 300)
    
    def validar_cajas(self):
        usuario = self.entry_usuario.get().strip()
        contraseña = self.entry_contraseña.get().strip()

        if not usuario or not contraseña:
            mostrar_alerta(self, "SECURITY BREACH", "¡Error! All fields are required.")
            return
        Ingreso_exitoso = self.db.verficar_login(usuario, contraseña)
        if Ingreso_exitoso:
            mostrar_alerta(self, "ACCESS GRANTED", "Welcome to Fazbear Entertainment!")
        else:
            mostrar_alerta(self, "ACCESS DENIED", "¡Error! Invalid username or password.")
    def abrir_registro(self):
        self.destroy()
        register_window = RegistroWindow()
        register_window.mainloop()


if __name__ == "__main__":
    app = LoginWindow() # Creo mi objeto de la clase que es donde hice la pantalla para cargar la pantalla
    app.mainloop() # Con mainloop mando pintar la ventana 