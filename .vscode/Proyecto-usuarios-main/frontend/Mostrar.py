import customtkinter as ctk 
from conexion import BaseDeDatos
from componentes import mostrar_alerta

class DashboardWindow(ctk.CTk):
    def __init__(self, rol_usuario):
        super().__init__()
        self.db = BaseDeDatos()
        self.rol_usuario = rol_usuario

        self.title("FAZBEAR ENTERTAINMENT - SECURITY TERMINAL")
        self.geometry("950x600")
        self.resizable(False, False)

        ctk.set_appearance_mode("Dark")
        self.configure(fg_color="#000000")

        self.configurar_elementos()
        self.cargar_datos()

    def configurar_elementos(self):

        self.lbl_titulo = ctk.CTkLabel(
            self, 
            text=f"SECURITY DASHBOARD — ACCESS LEVEL: {self.rol_usuario.upper()}", 
            font=("Courier New", 16, "bold"), 
            text_color="#FF1E3B"
        )
        self.lbl_titulo.pack(pady=15)

        self.scroll_tabla = ctk.CTkScrollableFrame(
            self, 
            width=890, 
            height=450, 
            fg_color="#121212", 
            border_color="#333333", 
            border_width=1
        )
        self.scroll_tabla.pack(pady=5, padx=20)

        self.btn_volver = ctk.CTkButton(
            self, 
            text="LOG OUT", 
            width=100, 
            height=30, 
            fg_color="#1A1A1A", 
            hover_color="#333333",
            text_color="#FFFFFF", 
            font=("Courier New", 11, "bold"),
            border_color="#555555",
            border_width=1,
            command=self.regresar_al_login
        )
        self.btn_volver.pack(side="bottom", pady=20)

    def cargar_datos(self):
        # Esto es para limpiar el scroll por si se recarga
        for widget in self.scroll_tabla.winfo_children():
            widget.destroy()
        
        # Sacamos los usuarios de la base de datos
        guardias = self.db.obtener_usuario(self.rol_usuario)
        
        # Por cualquier cosa de que este vacio y no haya guardias mostrar ese mensaje
        if not guardias:
            lbl_vacio = ctk.CTkLabel(
                self.scroll_tabla, 
                text="No security personnel records found in database.", 
                font=("Courier New", 12), 
                text_color="#888888"
            )
            lbl_vacio.pack(pady=20)
            return
        
        # iteramos los guardias que sacamos de la base de datos 
        for guardia in guardias:
            id_u = guardia[0]
            nombre = guardia[1]
            apellidos = guardia[2]
            curp = guardia[3]
            nss = guardia[4]
            rfc = guardia[5]
            usuario = guardia[6]
            telefono = guardia[7]
            rol = guardia[8]
            direccion = guardia[9]
            cp = guardia[10]
        
            card = ctk.CTkFrame(self.scroll_tabla, fg_color="#1A1A1A", border_color="#333333", border_width=1)
            card.pack(fill="x", padx=10, pady=8)

            info_texto = (
                f"User: {usuario} | Name: {nombre} {apellidos} | Role: {rol}\n"
                f"CURP: {curp} | NSS: {nss} | RFC: {rfc}\n"
                f"Phone: {telefono} | Address: {direccion} (CP: {cp})"
            )
        
            lbl_info = ctk.CTkLabel(
                card, 
                text=info_texto, 
                font=("Courier New", 11), 
                text_color="#CCCCCC", 
                justify="left"
            )
            lbl_info.pack(side="left", padx=15, pady=10)

            # Si el usuario es administrador activamos los botones de actualizar y eliminar 
            if self.rol_usuario == "Administrador":

                btn_eliminar = ctk.CTkButton(
                    card, 
                    text="DELETE", 
                    width=75, 
                    height=28, 
                    fg_color="#FF1E3B", 
                    hover_color="#990000",
                    font=("Courier New", 10, "bold"),
                    command=lambda id_reg=id_u, usr=usuario: self.confirmar_eliminacion(id_reg, usr)
                )
                btn_eliminar.pack(side="right", padx=5)

                btn_modificar = ctk.CTkButton(
                    card, 
                    text="EDIT", 
                    width=75, 
                    height=28, 
                    fg_color="#333333", 
                    hover_color="#555555",
                    font=("Courier New", 10, "bold"),
                    command=lambda datos=guardia: self.abrir_ventana_editar(datos)
                )
                btn_modificar.pack(side="right", padx=5)

    def confirmar_eliminacion(self, id_usuario, nombre_usuario):
        exito = self.db.eliminar_usuario(id_usuario, self.rol_usuario)
        if exito:
            mostrar_alerta(self, "SUCCESS", f"Guard {nombre_usuario} removed from database.")
            self.cargar_datos()
        else:
            mostrar_alerta(self, "SECURITY ERROR", "Access denied or failed to delete record.")
    
    def abrir_ventana_editar(self, guardia):
        
        id_u = guardia[0]
        tel_actual = guardia[7]
        dir_actual = guardia[9]
        cp_actual = guardia[10]
        rol_actual = guardia[8]

        edit_win = ctk.CTkToplevel(self)
        edit_win.title(f"EDIT GUARD — ID {id_u}")
        edit_win.geometry("400x420")
        edit_win.resizable(False, False)
        edit_win.configure(fg_color="#000000")
        edit_win.grab_set() # Esta de aqui bloquea la ventana priincipal mientras estas editando

        ctk.CTkLabel(edit_win, text="UPDATE SECURITY PERSONNEL", font=("Courier New", 14, "bold"), text_color="#FF1E3B").pack(pady=15)

        # Teléfono
        ctk.CTkLabel(edit_win, text="Phone:", font=("Courier New", 11, "bold"), text_color="#CCCCCC").pack(anchor="w", padx=30)
        entry_tel = ctk.CTkEntry(edit_win, width=340, height=30, fg_color="#1A1A1A", text_color="#FFFFFF")
        entry_tel.pack(padx=30, pady=(0, 10))
        entry_tel.insert(0, str(tel_actual))

        # Dirección
        ctk.CTkLabel(edit_win, text="Address:", font=("Courier New", 11, "bold"), text_color="#CCCCCC").pack(anchor="w", padx=30)
        entry_dir = ctk.CTkEntry(edit_win, width=340, height=30, fg_color="#1A1A1A", text_color="#FFFFFF")
        entry_dir.pack(padx=30, pady=(0, 10))
        entry_dir.insert(0, str(dir_actual))

        # Código Postal
        ctk.CTkLabel(edit_win, text="Zip Code:", font=("Courier New", 11, "bold"), text_color="#CCCCCC").pack(anchor="w", padx=30)
        entry_cp = ctk.CTkEntry(edit_win, width=340, height=30, fg_color="#1A1A1A", text_color="#FFFFFF")
        entry_cp.pack(padx=30, pady=(0, 10))
        entry_cp.insert(0, str(cp_actual))

        # Rol
        ctk.CTkLabel(edit_win, text="Role:", font=("Courier New", 11, "bold"), text_color="#CCCCCC").pack(anchor="w", padx=30)
        combo_rol = ctk.CTkComboBox(edit_win, values=["Administrador", "Empleado"], width=340, height=30, fg_color="#1A1A1A")
        combo_rol.pack(padx=30, pady=(0, 20))
        combo_rol.set(rol_actual)

        def guardar_cambios():

            nuevo_tel = entry_tel.get().strip()
            nueva_dir = entry_dir.get().strip()
            nuevo_cp = entry_cp.get().strip()
            nuevo_rol = combo_rol.get()

            exito = self.db.actualizar_usuario(id_u, nuevo_tel, nueva_dir, nuevo_cp, nuevo_rol, self.rol_usuario)
            if exito:
                mostrar_alerta(self, "SUCCESS", "Guard updated successfully.")
                edit_win.destroy()
                self.cargar_datos() # Refrescamos la vista principal
            else:
                mostrar_alerta(self, "DATABASE ERROR", "Failed to update record.")
        
        btn_guardar = ctk.CTkButton(
            edit_win, 
            text="SAVE CHANGES", 
            width=200, 
            height=35, 
            fg_color="#1A1A1A", 
            hover_color="#333333",
            text_color="#FFFFFF",
            font=("Courier New", 12, "bold"),
            border_color="#555555",
            border_width=1,
            command=guardar_cambios
        )
        btn_guardar.pack(pady=10)

    def regresar_al_login(self):
        from login import LoginWindow
        self.destroy() 
        login_app = LoginWindow() 
        login_app.mainloop()


