from tkinter import *
import sqlite3 as sql



# Creamos la base de datos que vamos a usar en la aplicación


def crearTabla():
    conexion = sql.connect("actividad10.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Datos (Usuario TEXT, Correo TEXT, Contraseña TEXT)")
    conexion.commit()
    cursor.close()
    conexion.close()

crearTabla()

#Funciones para olvidar datos registrados 

def olvidar(elemento):
  
    elemento.forget()


def cerrar(elemento):
  
    elemento.destroy()




#Establecemos la página principal del programa


def inicio():

    global ventanaInicio
    ventanaInicio = Tk()
    ventanaInicio.title("Inicio")
    ventanaInicio.geometry("500x500")

     

    Label(ventanaInicio, text="Acceso al sistema", bg="navy", fg="white", width="50", height="3", font=("Calibri", 15)).pack()
    Label(ventanaInicio, text="").pack()   

    Button(ventanaInicio, text = "Registro", height="3", width="30", command = registro).pack()
    Label(ventanaInicio, text = "").pack()

    Button(ventanaInicio, text = "Login ", height="3", width="30", command = login).pack()
    Label(ventanaInicio, text = "").pack()


    ventanaInicio.mainloop()




#Establecemos la conexión con la base de datos e introducimos los valores.


def registroDatos():
    infoUsuario = usuario.get()
    infoContrasena = contrasena.get() 
    infoCorreo = correo.get()
   

    if infoCorreo and infoUsuario and infoContrasena:

        conexion = sql.connect("actividad10.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Datos values(\'"+infoUsuario+"\',\'"+infoCorreo+"\',\'"+infoContrasena+"')")
        conexion.commit()
        cursor.close()
        conexion.close()

        Label(ventanaRegistro, text= "Registro correcto").pack()
        Label(ventanaRegistro, text= " ").pack()
        Button(ventanaRegistro, text="Login", height="3", width="30", command = lambda : [cerrar(ventanaRegistro), login()]).pack()
        Label(ventanaRegistro, text = "").pack()
    
    else: 

        Label(ventanaRegistro, text= "Registro incorrecto").pack()
        Button(ventanaRegistro, text="Intentarlo de nuevo", height="3", width="30", command = lambda : [cerrar(ventanaRegistro), registro()]).pack()
        Label(ventanaRegistro, text = "").pack() 
    



#Establecemos la página de registro del programa


def registro():

    global ventanaRegistro
    ventanaRegistro = Toplevel(ventanaInicio)
    ventanaRegistro.title("Registro")
    ventanaRegistro.geometry("500x500")



    Label(ventanaRegistro, text="Por favor introduzca los siguientes datos:", bg="navy", fg="white", width="50", height="3", font=("Calibri", 15)).pack()
    Label(ventanaRegistro, text="").pack()

    global usuario
    global contrasena
    global correo

    usuario = StringVar()
    contrasena = StringVar()
    correo = StringVar()

    global registroUsuario
    global registroContrasena
    global registroCorreo


    Label(ventanaRegistro, text="Usuario").pack()
    registroUsuario = Entry(ventanaRegistro, textvariable = usuario).pack()


    Label(ventanaRegistro, text="Correo electrónico").pack()
    registroCorreo = Entry(ventanaRegistro, textvariable = correo).pack()


    Label(ventanaRegistro, text="Contraseña" ).pack()
    registroContrasena = Entry(ventanaRegistro, textvariable= contrasena, show = "*").pack()

    Label(ventanaRegistro, text= "").pack()
    botonRegistro = Button(ventanaRegistro, text="Continuar",height="3", width="30" , command = lambda : [registroDatos(), olvidar(botonRegistro)] )
    botonRegistro.pack()
    
    Label(ventanaRegistro, text = "").pack()
    



#Establecemos las opciones de logeo.


def logeo():

    correoLogin = correo2.get()
    contrasenaLogin = contrasena2.get()

    conexion = sql.connect("actividad10.db")
    cursor = conexion.cursor()  
    cursor.execute('SELECT * FROM Datos WHERE Correo = ? AND Contraseña = ?',(correoLogin,contrasenaLogin))
   
    if cursor.fetchall():
            Label(ventanaLogin, text= "Login correcto" ).pack()
            Button(ventanaLogin, text="Continuar", height="3", width="30",  command = lambda : [cerrar(ventanaLogin), final()]).pack()
            Label(ventanaLogin, text = "").pack()
     
    else:

            Label(ventanaLogin, text= "Login incorrecto" ).pack()
            Button(ventanaLogin, text="Intentarlo de nuevo", height="3", width="30",  command = lambda : [cerrar(ventanaLogin), login()]).pack()
            Label(ventanaLogin, text = "").pack()
   
    cursor.close()
    conexion.close()




#Establecemos la página de login del programa.


def login():

    global ventanaLogin
    ventanaLogin = Toplevel(ventanaInicio)
    ventanaLogin.title("Login")
    ventanaLogin.geometry("500x500")


    Label(ventanaLogin, text="Por favor introduzca los siguientes datos:", bg="navy", fg="white", width="50", height="3", font=("Calibri", 15)).pack()
    Label(ventanaLogin, text="").pack()

    global contrasena2
    global correo2


    contrasena2 = StringVar()
    correo2 = StringVar()

    global loginContrasena
    global loginCorreo


    Label(ventanaLogin, text="Correo electrónico").pack()
    loginCorreo = Entry(ventanaLogin, textvariable = correo2).pack()

    Label(ventanaLogin, text="Contraseña" ).pack()
    loginContrasena = Entry(ventanaLogin, textvariable= contrasena2, show = "*").pack()



    Label(ventanaLogin, text= " ").pack()
    botonLogin = Button(ventanaLogin, text="Continuar",height="3", width="30" , command = lambda : [logeo(), olvidar(botonLogin)] )
    botonLogin.pack()
    Label(ventanaLogin, text = "").pack()





#Establecemos la página final del programa.


def final():

    global ventanaFinal
    ventanaFinal = Toplevel(ventanaInicio)
    ventanaFinal.title("Fin")
    ventanaFinal.geometry("500x500")



    Label(ventanaFinal, text="Acceso completado", bg="navy", fg="white", width="50", height="3", font=("Calibri", 15)).pack()
    Label(ventanaFinal, text="").pack()   
    Label(ventanaFinal, text="Bienvenido :)").pack()   
    Label(ventanaFinal, text="").pack()   





inicio()