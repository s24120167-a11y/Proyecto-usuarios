import customtkinter as ctk
from componentes import mostrar_alerta
from conexion import BaseDeDatos

class RegistroWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db = BaseDeDatos()

        self.title("FAZBEAR ENTERTAINMENT - NEW GUARD REGISTRATION")
        self.geometry("600x650")
        self.resizable(False, False)

        # Configuracion de diseño
        ctk.set_appearance_mode("Dark")
        self.configure(fg_color="#000000")

        self.configurar_elementos()

    def configurar_elementos(self):
        
        # Título principal
        self.lbl_titulo = ctk.CTkLabel(
            self, 
            text="SECURITY PERSONNEL REGISTRATION", 
            font=("Courier New", 18, "bold"), 
            text_color="#FFFFFF"
        )
        self.lbl_titulo.pack(pady=(20, 5))
    
        self.lbl_sub = ctk.CTkLabel(
            self, 
            text="Fill in all database fields for Azure storage", 
            font=("Courier New", 10, "bold"), 
            text_color="#FF1E3B"
        )
        self.lbl_sub.pack(pady=(0, 15))
        
        # El ScrollabeFrame es para agrupar varios elementos como cajas de texto y labels o asi adentro de el
        # es para que se vea mas ordenado y bonito es el cuadrito que se ve que se puede deslizar arriba y abajo
        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            width=520,
            height=460,
            fg_color="#121212", 
            border_color="#333333", 
            border_width=1
        )
        self.scroll_frame.pack(pady=5, padx=20)

        # Campos del formulario
        # Nombre
        self.lbl_nombre = ctk.CTkLabel(self.scroll_frame, text="Name(s):", font=("Courier New", 11, "bold"), text_color="#CCCCCC")
        self.lbl_nombre.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_nombre = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_nombre.pack(padx=20)

        # Apellidos
        self.lbl_apellidos = ctk.CTkLabel(self.scroll_frame, text="Lastname:", font=("Courier New", 11, "bold"), text_color="#CCCCCC")
        self.lbl_apellidos.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_apellidos = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_apellidos.pack(padx=20)

        # Correo Electrónico
        self.lbl_correo = ctk.CTkLabel(self.scroll_frame, text="Email:", font=("Courier New", 11, "bold"), text_color="#CCCCCC")
        self.lbl_correo.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_correo = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_correo.pack(padx=20)

        # Teléfono
        self.lbl_telefono = ctk.CTkLabel(self.scroll_frame, text="Phone number:", font=("Courier New", 11, "bold"), text_color="#CCCCCC")
        self.lbl_telefono.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_telefono = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_telefono.pack(padx=20)

        # Dirección
        self.lbl_direccion = ctk.CTkLabel(self.scroll_frame, text="Address:", font=("Courier New", 11, "bold"), text_color="#CCCCCC")
        self.lbl_direccion.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_direccion = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_direccion.pack(padx=20)

        # Código Postal
        self.lbl_cp = ctk.CTkLabel(self.scroll_frame, text="Zip Code (5 digits):", font=("Courier New", 11, "bold"), text_color="#CCCCCC")
        self.lbl_cp.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_cp = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_cp.pack(padx=20, pady=(0, 20))

        # CURP
        self.lbl_curp = ctk.CTkLabel(self.scroll_frame, text="CURP (18 characters):", font=("Courier New", 11, "bold"), text_color="#FF1E3B")
        self.lbl_curp.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_curp = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_curp.pack(padx=20)

        # NSS 
        self.lbl_nss = ctk.CTkLabel(self.scroll_frame, text="NSS (11 digits):", font=("Courier New", 11, "bold"), text_color="#FF1E3B")
        self.lbl_nss.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_nss = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_nss.pack(padx=20)

        # RFC
        self.lbl_rfc = ctk.CTkLabel(self.scroll_frame, text="RFC (12 characters):", font=("Courier New", 11, "bold"), text_color="#FF1E3B")
        self.lbl_rfc.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_rfc = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_rfc.pack(padx=20)

        # Usuario
        self.lbl_usuario = ctk.CTkLabel(self.scroll_frame, text="User (Unique):", font=("Courier New", 11, "bold"), text_color="#FF1E3B")
        self.lbl_usuario.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_usuario = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11))
        self.entry_usuario.pack(padx=20)

        # Password
        self.lbl_password = ctk.CTkLabel(self.scroll_frame, text="Password:", font=("Courier New", 11, "bold"), text_color="#FF1E3B")
        self.lbl_password.pack(anchor="w", padx=20, pady=(10, 2))
        self.entry_password = ctk.CTkEntry(self.scroll_frame, width=460, height=32, fg_color="#1A1A1A", text_color="#FFFFFF", font=("Courier New", 11), show="*")
        self.entry_password.pack(padx=20)

        # Rol
        self.lbl_rol = ctk.CTkLabel(self.scroll_frame, text="System Rol:", font=("Courier New", 11, "bold"), text_color="#CCCCCC")
        self.lbl_rol.pack(anchor="w", padx=20, pady=(10, 2))
        self.combo_rol = ctk.CTkComboBox(self.scroll_frame, values=["Administrador", "Empleado"], width=460, height=32, fg_color="#1A1A1A", button_color="#333333", text_color="#FFFFFF")
        self.combo_rol.pack(padx=20)
        self.combo_rol.set("Empleado")

        # Boton de registro 
        self.btn_registrar = ctk.CTkButton(
            self, 
            text="REGISTER GUARD", 
            width=260, 
            height=40, 
            fg_color="#1A1A1A", 
            hover_color="#333333",
            text_color="#FFFFFF", 
            font=("Courier New", 14, "bold"),
            border_color="#555555",
            border_width=1,
            command=self.validar_registro
        )
        self.btn_registrar.pack(pady=15)
    
    def validar_registro(self):
        
        nombre = self.entry_nombre.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        correo = self.entry_correo.get().strip()
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()
        rol = self.combo_rol.get()
        telefono = self.entry_telefono.get().strip()
        curp = self.entry_curp.get().strip()
        nss = self.entry_nss.get().strip()
        rfc = self.entry_rfc.get().strip()
        direccion = self.entry_direccion.get().strip()
        cp = self.entry_cp.get().strip()
        
        # Validación 1: Todos lo campos deben estar llenos
        if not all([nombre, apellidos, correo, usuario, password, telefono, curp, nss, rfc, direccion, cp]):
            mostrar_alerta(self, "SECURITY BREACH", "¡Error! All fields are required.")
            return
        # Validación 2: Longitudes exactas
        if len(curp) != 18:
            mostrar_alerta(self, "VALIDATION ERROR", "The CURP must have exactly 18 characters.")
            return

        if len(nss) != 11:
            mostrar_alerta(self, "VALIDATION ERROR", "The NSS must have exactly 11 digits.")
            return

        if len(rfc) != 12:
            mostrar_alerta(self, "VALIDATION ERROR", "The RFC must have exactly 12 characters.")
            return

        if len(cp) != 5:
            mostrar_alerta(self, "VALIDATION ERROR", "The zip Code must have 5 digits.")
            return
        
        mostrar_alerta(self, "SUCCESS", f"Guardia {usuario} successfully validated.")

        datos_usuario = (nombre, apellidos, correo, telefono, direccion, cp, curp, nss, rfc, usuario, password, rol)
        successful = self.db.ingresar_usuario(*datos_usuario)
        if successful:
            mostrar_alerta(self, "SUCCESS", f"Guardia {usuario} successfully registered in the database.")
        else:
            mostrar_alerta(self, "DATABASE ERROR", "Failed to register the guard in the database.")

if __name__ == "__main__":
    app = RegistroWindow()
    app.mainloop()
    