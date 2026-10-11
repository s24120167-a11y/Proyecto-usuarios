import mysql.connector as mysql_connector # este seria el paquete que utilizamos para hacer la conexion de mysql a python

class base_datos:
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
    def ingresar_usuario(self, nombre, apellidos,correo,telefono,direccion,cp,curp,nss,rfc,usuario,contrasena,rol):
        conexion = self.conectar()
        if conexion is None:
            return False
        try:
            cursor = conexion.cursor()# A este punto llamamos la funcion conectar y aqui es la conexion utilizada pata el registro
            consulta = "INSERT INTO usuarios (nombre, apellidos, correo, telefono,direccion,cp,curp,nss,rfc,usuario,contrasena,rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (nombre, apellidos, correo, telefono, direccion, cp, curp, nss, rfc, usuario, contrasena, rol)
            cursor.execute(consulta, valores)
            conexion.commit()#Este guarda los cambios en la base de datos 
            return True
        except mysql_connector.Error as error:
            print(f"Error al ingresar el usuario: {error}")
            return False
        finally:
            if  conexion.is_connected():
                cursor.close()#Esta linea termina cerrando la conexion cuando finaliza el programa para que no sature la base o consuma recursos 
                conexion.close()
    def verficar_login(self,usuario,password):
        conexion = self.conectar()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            consulta = "select * from usuarios where usuario = %s and password = %s"
            cursor.execute(consulta,(usuario,password))
            resultado = cursor.fetchone()# Esta funcion es para recuperar solo un dato de la fila a la que estamos accediendo 
            return resultado is not None# tambien esta fetchall pero esa se puede usar para cuando manejas multiples datos 
        except mysql_connector.connector.Error as error:
            print(f"Error al verificar el usuario: {error}")
            return False
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    