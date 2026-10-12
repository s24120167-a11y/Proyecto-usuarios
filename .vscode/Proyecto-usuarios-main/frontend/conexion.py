import mysql.connector as mysql_connector # este seria el paquete que utilizamos para hacer la conexion de mysql a python
import hashlib # libreria de python para hashear con sha2 y asi
from cryptography.fernet import Fernet # libreria de python para encriptar datos 

class BaseDeDatos:
    def __init__(self):
        self.CLAVE_ENCRYPT = b'X9vLp3_K8wR2zY5sN1mQ4tJ7fH6dC0bV8xN2m_L4pK8=' # con esto desemcriptamos
        try: 
            self.cipher = Fernet(self.CLAVE_ENCRYPT)
        except Exception:
            self.key = Fernet.generate_key()
            self.cipher = Fernet(self.key)

    def conectar(self): #Agregamos una clase donde va a venir toda la conexion hacia la base de datos 
        try:
            conexion = mysql_connector.connect(
            host = "servidor2026.mysql.database.azure.com", # Se ingresan los datos de la conexion como 
            user = "Leo",# El host,usuario, contraseña y la base se podria usar un constructor para poder cambiar de base 
            password = "root123+",# Pero lo dejamos asi por el momento 
            database = "usuarios" )
            return conexion 
        except mysql_connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
            return None

    def hasehar_password(self, password):
        return hashlib.sha512(password.encode('utf-8')).hexdigest()
    
    def cifrar_dato(self, texto):
        if not texto:
            return ""
        return self.cipher.encrypt(texto.encode('utf-8')).decode('utf-8')
    
    def descifrar_texto(self, texto_cifrado):
        if not texto_cifrado:
            return ""
        try:
            return self.cipher.decrypt(texto_cifrado.encode('utf-8')).decode('utf-8')
        except Exception:
            return texto_cifrado

    def ingresar_usuario(self, nombre, apellidos,correo,telefono,direccion,cp,curp,nss,rfc,usuario,contrasena,rol):
        conexion = self.conectar()
        if conexion is None:
            return False
        
        password_hash = self.hasehar_password(contrasena)
        
        curp_cifrado = self.cifrar_dato(curp)
        nss_cifrado = self.cifrar_dato(nss)
        rfc_cifrado = self.cifrar_dato(rfc)

        try:
            cursor = conexion.cursor()# A este punto llamamos la funcion conectar y aqui es la conexion utilizada pata el registro
            consulta = """ 
                INSERT INTO usuarios 
                (nombre, apellidos, curp, nss, rfc, usuario, password, telefono, rol, direccion, codigoPostal, correoElectronico) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (nombre, apellidos, curp_cifrado, nss_cifrado, rfc_cifrado, usuario, password_hash, telefono, rol, direccion, cp, correo)
            cursor.execute(consulta, valores)
            conexion.commit() #Este guarda los cambios en la base de datos 
            return True
        except mysql_connector.Error as error:
            print(f"Error al ingresar el usuario: {error}")
            return False
        finally:
            if  conexion.is_connected():
                cursor.close()#Esta linea termina cerrando la conexion cuando finaliza el programa para que no sature la base o consuma recursos 
                conexion.close()


    def verficar_login(self, usuario, password):
        conexion = self.conectar()
        if not conexion:
            return None
        
        password_hash = self.hasehar_password(password)

        try:
            cursor = conexion.cursor()
            consulta = "select rol from usuarios where usuario = %s and password = %s"
            cursor.execute(consulta,(usuario, (password_hash)))
            resultado = cursor.fetchone()# Esta funcion es para recuperar solo un dato de la fila a la que estamos accediendo 
            # return resultado is not None# tambien esta fetchall pero esa se puede usar para cuando manejas multiples datos 
        
            if resultado:
                return resultado[0]
            return None

        except mysql_connector.connector.Error as error:
            print(f"Error al verificar el usuario: {error}")
            return None
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
    
    def obtener_usuario(self, rol_usuario_actual):
        conexion = self.conectar()
        if not conexion:
            return []
        
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, apellidos, curp, nss, rfc, usuario, telefono, rol, direccion, codigoPostal FROM usuarios")
        resultados = cursor.fetchall()
        
        usuarios_procesados = []
        for row in resultados:
            lista_fila = list(row)
            
            if rol_usuario_actual == "Administrador":
                try:
                    lista_fila[3] = self.descifrar_texto(lista_fila[3])
                    lista_fila[4] = self.descifrar_texto(lista_fila[4])
                    lista_fila[5] = self.descifrar_texto(lista_fila[5])
                except Exception:
                    pass
            else:
                lista_fila[3] = "XXXX-XXXX-XXXXXX"
                lista_fila[4] = "XXXXXXXXXXX"
                lista_fila[5] = "XXXX-XXXXXX-XXX"
            
            usuarios_procesados.append(tuple(lista_fila))
            
        cursor.close()
        conexion.close()
        return usuarios_procesados
                
    
    def actualizar_usuario(self, id_usuario, telefono, direccion, cp, rol, rol_usuario):
        if rol_usuario != "Administrador":
            print("ACCESO DENEGADO: Los empleados no pueden actualizar registros.")
            return False
        conexion = self.conectar()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            consulta = """
                UPDATE usuarios
                SET telefono = %s, direccion = %s, codigoPostal = %s, rol = %s
                WHERE id = %s
            """
            valores = (telefono, direccion, cp, rol, id_usuario)
            cursor.execute(consulta, valores)
            conexion.commit()
            return True
        except mysql_connector.Error as error:
            print(f"Error updating user: {error}")
            return False
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
    
    def eliminar_usuario(self, id_usuario, rol_usuario):
        if rol_usuario != "Administrador":
            print("ACCESO DENEGADO: Los empleados no pueden eliminar registros.")
            return False
        conexion = self.conectar()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(consulta, (id_usuario,))
            conexion.commit()
            return True
        except mysql_connector.Error as error:
            print(f"Error deleting user: {error}")
            return False
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()


    