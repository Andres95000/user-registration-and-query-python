from tkinter import *
from tkinter import messagebox
import sqlite3

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

    if valor == "yes":
        root.destroy()

def limpiarCampos():
    miNombre.set("")
    misApellidos.set("")
    miID.set("")
    miPassword.set("")
    miDireccion.set("")
    textComentarios.delete(1.0, END)

def conexionBBDD():
    try:
        conn = sqlite3.connect("base_Datos_Registro.db")
    except:
        print("Base datos ya existe")

    myCursor = conn.cursor()

    try:
        myCursor.execute('''CREATE TABLE Registros_Personas (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(50),
            Apellidos VARCHAR(50),
            Passwrd VARCHAR(20),
            Direccion VARCHAR(20) UNIQUE,
            Comentarios VARCHAR (200))''')
        messagebox.showinfo("Base de datos", "Base de datos creada exitosamente.")
    except:
        messagebox.showwarning("¡Atencion!", "La base de datos ya existe")

def created():
    conn = sqlite3.connect("base_Datos_Registro.db")
    myCursor = conn.cursor()

    """myCursor.execute(f"INSERT INTO Registros_Personas VALUES(NULL, '" + miNombre.get() + "','" + misApellidos.get() + "','" + miPassword.get() + "','" + miDireccion.get() + "','" + textComentarios.get("1.0", END) + "')")# Utilizar las ?,?,?,?"""

    datos = miNombre.get(), misApellidos.get(), miPassword.get(), miDireccion.get(), textComentarios.get("1.0", END)

    myCursor.execute("INSERT INTO Registros_Personas VALUES(NULL, ?,?,?,?,?)", (datos)) #De forma para metrizada, para mas seguridad

    conn.commit()

    messagebox.showinfo("Base de datos", "Registro ingresado exitosamente")

def read():
    conn = sqlite3.connect("base_Datos_Registro.db")
    myCursor = conn.cursor()

    myCursor.execute(f"SELECT * FROM Registros_Personas WHERE ID = " + miID.get())

    elUsuario = myCursor.fetchall()

    if elUsuario == []:
        messagebox.showinfo("Base de datos", "El usuario no se encuentra en la base de datos")
    else:
        for usuario in elUsuario:
            miID.set(usuario[0])
            miNombre.set(usuario[1])
            misApellidos.set(usuario[2])
            miPassword.set(usuario[3])
            miDireccion.set(usuario[4])
            textComentarios.insert(1.0, usuario[5])

        messagebox.showinfo("Base de datos", "Busqueda finalizada")

    conn.commit()



def update():
    conn = sqlite3.connect("base_Datos_Registro.db")
    myCursor = conn.cursor()

    """myCursor.execute(f"UPDATE Registros_Personas SET Nombre = '" + miNombre.get() + "', Apellidos = '" + misApellidos.get() + "', Passwrd = '" + miPassword.get() + "', Direccion ='" + miDireccion.get() + "', Comentarios = '" + textComentarios.get("1.0", END) + "' WHERE ID = " + miID.get())# Utilizar las ?,?,?,?"""

    datos = miNombre.get(), misApellidos.get(), miPassword.get(), miDireccion.get(), textComentarios.get("1.0", END)

    myCursor.execute("UPDATE Registros_Personas SET Nombre = ?, Apellidos = ?, Passwrd = ?, Direccion =?, Comentarios = ?" + "WHERE ID ="+ miID.get(), (datos)) #De forma para metrizada, para mas seguridad

    conn.commit()

    messagebox.showinfo("Base de datos", "Registro actualizado exitosamente")

def eliminate():
    conn = sqlite3.connect("base_Datos_Registro.db")
    myCursor = conn.cursor()

    valor = messagebox.askquestion("Eliminar usuario", "¿Estas seguro de eliminar usuario?")

    if valor == "yes":
        myCursor.execute(f"DELETE FROM Registros_Personas WHERE ID =" + miID.get())

    conn.commit()

    


root = Tk()
root.config(bg = "#212121")
root.title("Formulario de Registro")
root.iconbitmap("contrato.ico")

#----------------------------------Variables---------------------------#
miID = StringVar()
miNombre = StringVar()
misApellidos = StringVar()
miDireccion = StringVar()
miPassword = StringVar()

#----------------------------------Frame Formulario---------------------------#

frameContainer = LabelFrame(root, text="Formulario")
frameContainer.pack(fill= "both", expand = "yes", padx= 20, pady=20)
frameContainer.config(bg = "#212121", fg = "#ffffff")

#-----------------------------------ID-----------------------------------#
labelId = Label(frameContainer, text = "ID")
labelId.grid(row = 0 , column = 0, padx= 5, pady=5)
labelId.config(bg = "#212121", fg = "#ffffff")

entryID = Entry(frameContainer, textvariable= miID)
entryID.grid(row = 0, column =1, padx= 5, pady=5)
entryID.config(bg = "#646160", fg = "#ffffff")

#-----------------------------------Nombre-----------------------------------#
labelNombre = Label(frameContainer, text = "Nombre")
labelNombre.grid(row = 0 , column = 2, padx= 5, pady=5)
labelNombre.config(bg = "#212121", fg = "#ffffff")

entryNombre = Entry(frameContainer, textvariable=miNombre)
entryNombre.grid(row = 0, column =3, padx= 5, pady=5)
entryNombre.config(bg = "#646160", fg = "#ffffff")

#-----------------------------------Apellidos--------------------------------#
labelApellidos = Label(frameContainer, text = "Apellidos")
labelApellidos.grid(row = 0 , column = 4, padx= 5, pady=5)
labelApellidos.config(bg = "#212121", fg = "#ffffff")

entryApellidos = Entry(frameContainer, textvariable= misApellidos)
entryApellidos.grid(row = 0, column =5, padx= 5, pady=5)
entryApellidos.config(bg = "#646160", fg = "#ffffff")

#-----------------------------------Password---------------------------------#
labelPassword = Label(frameContainer, text = "Password")
labelPassword.grid(row = 1 , column = 0, padx= 5, pady=5)
labelPassword.config(bg = "#212121", fg = "#ffffff")

entryPassword = Entry(frameContainer, textvariable= miPassword)
entryPassword.grid(row = 1, column =1, padx= 5, pady=5)
entryPassword.config(bg = "#646160", fg = "#ffffff", show = "*")

#-----------------------------------Direccion--------------------------------#
labelDireccion = Label(frameContainer, text = "Direccion")
labelDireccion.grid(row = 1 , column = 2, padx= 5, pady=5)
labelDireccion.config(bg = "#212121", fg = "#ffffff")

entryDireccion = Entry(frameContainer, textvariable= miDireccion)
entryDireccion.grid(row = 1, column =3, padx= 5, pady=5)
entryDireccion.config(bg = "#646160", fg = "#ffffff")

#-----------------------------------Comentarios------------------------------#
labelComentarios = Label(frameContainer, text = "Comentarios")
labelComentarios.grid(row = 2 , column = 0, sticky = "n", padx= 5, pady=5)
labelComentarios.config(bg = "#212121", fg = "#ffffff")

textComentarios = Text(frameContainer, height = 5, width = 25)
textComentarios.grid(row = 2 , column = 1, columnspan = 2, padx= 5, pady=5)
textComentarios.config(bg = "#646160", fg = "#ffffff")

#----------------------------------Frame Botones---------------------------#
frameBotones = Frame(root)
frameBotones.pack(fill= "both", expand = "yes", padx= 20, pady=20)
frameBotones.config(bg = "#212121")

#-----------------------------------Boton Crear(Create)------------------------------#
btnCrear = Button(frameBotones, text = "Crear Usuario")
btnCrear.grid(row = 0, column = 0, padx= 15, pady=15)
btnCrear.config(bg = "#413F3E", fg = "#ffffff", activebackground = "#000000", activeforeground = "#ffffff", command= created)

#-----------------------------------Boton Buscar(Read)------------------------------#
btnBuscar = Button(frameBotones, text = "Buscar Usuario")
btnBuscar.grid(row = 0, column = 1, padx= 15, pady=15)
btnBuscar.config(bg = "#413F3E", fg = "#ffffff", activebackground = "#000000", activeforeground = "#ffffff", command= read)

#-----------------------------------Boton Actualizar(Update)------------------------------#
btnActualizar = Button(frameBotones, text = "Actualizar Usuario")
btnActualizar.grid(row = 0, column = 2, padx= 15, pady=15)
btnActualizar.config(bg = "#413F3E", fg = "#ffffff", activebackground = "#000000", activeforeground = "#ffffff", command= update)

#-----------------------------------Boton Eliminar(Delete)------------------------------#
btnEliminar = Button(frameBotones, text = "Eliminar Usuario")
btnEliminar.grid(row = 0, column = 3, padx= 15, pady=15)
btnEliminar.config(bg = "#413F3E", fg = "#ffffff", activebackground = "#000000", activeforeground = "#ffffff", command= eliminate)

#-----------------------------------Boton Conectar------------------------------#
btnConectar = Button(frameBotones, text = "Conectar base de datos")
btnConectar.grid(row = 1, column = 0, padx= 15, pady=15)
btnConectar.config(bg = "#413F3E", fg = "#ffffff", activebackground = "#000000", activeforeground = "#ffffff", command= conexionBBDD)

#-----------------------------------Boton Conectar------------------------------#
btnConectar = Button(frameBotones, text = "Limpiar campos")
btnConectar.grid(row = 1, column = 1, padx= 15, pady=15)
btnConectar.config(bg = "#413F3E", fg = "#ffffff", activebackground = "#000000", activeforeground = "#ffffff", command= limpiarCampos)

#-----------------------------------Boton Salir------------------------------#
btnConectar = Button(frameBotones, text = "Salir")
btnConectar.grid(row = 1, column = 2, padx= 15, pady=15)
btnConectar.config(bg = "#FF4040", fg = "#ffffff", activebackground = "#FF1C1C", activeforeground = "#ffffff", command= salirAplicacion)


root.mainloop()