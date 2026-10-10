import customtkinter as ctk

def mostrar_alerta(parent, titulo, mensaje):
        # Ventana emergente personalizada
        popup = ctk.CTkToplevel(parent)
        popup.title(titulo)
        popup.geometry("380x180") # Tamaño de la ventana
        popup.resizable(False, False)
        popup.configure(fg_color="#000000") # Color de fondo de la ventana

        # Bloquea la ventana de atrás hasta cerrarla
        popup.transient(parent)
        popup.grab_set()

        # Calculamos la posición exacta para centrarla sobre la ventana de login
        parent.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() - 380) // 2
        y = parent.winfo_y() + (parent.winfo_height() - 180) // 2
        popup.geometry(f"+{x}+{y}")

        # Título de la alerta 
        lbl_titulo = ctk.CTkLabel(
            popup, 
            text=titulo.upper(), 
            font=("Courier New", 14, "bold"), 
            text_color="#FF1E3B"
        )
        lbl_titulo.pack(pady=(20, 10))

        # Mensaje de error y información
        lbl_msg = ctk.CTkLabel(
            popup, 
            text=mensaje, 
            font=("Courier New", 11), 
            text_color="#FFFFFF",
            wraplength=340,
            justify="center"
        )
        lbl_msg.pack(pady=5)

        btn_ok = ctk.CTkButton(
            popup, 
            text="OK", 
            width=120, 
            height=32, 
            fg_color="#1A1A1A", 
            hover_color="#333333",
            border_color="#FF1E3B",
            border_width=1,
            text_color="#FFFFFF",
            font=("Courier New", 12, "bold"),
            command=popup.destroy
        )
        btn_ok.pack(pady=(15, 20))