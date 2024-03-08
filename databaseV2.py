import mysql.connector as my
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from PIL import Image,ImageTk
from tkinter import filedialog
import shutil
import os
import cv2
import time
import serial as s

def reset(): #deja en blanco los inputs
        inputModel.delete(0,tk.END)
        inputName.delete(0,tk.END)
        selection.set("Seleccionar")
        inputMarca.delete(0,tk.END)
        inputMaterial.delete(0,tk.END)
        inputColor.delete(0,tk.END)
        inputPrecio.delete(0,tk.END)
        inputCosto.delete(0,tk.END)
        dateInput.delete(0,tk.END)
        dateInput.insert(0,"yyyy/mm/dd")
        stockInput.delete(0,tk.END)
 
def retornarId():
    task.execute(f"SELECT Id_Producto FROM Producto WHERE Nom_producto = '{inputName.get()}' AND Modelo = '{inputModel.get()}' AND Color = '{inputColor.get()}'")
    temp=task.fetchone()
    if temp is not None:
        id_Producto=temp[0]
    else:
        id_Producto=0
    return id_Producto

def retornarIdCategoria():
    task.execute(f"SELECT Id_Categoria FROM Categoria WHERE Nombre_Categoria = '{selection.get()}'")
    temp=task.fetchone()
    if temp is not None:
        id_Categoria=temp[0]
    else:
        id_Categoria=0
    return id_Categoria

def retornarIdProveedor():
    task.execute(f"SELECT Id_Proveedor FROM Proveedor WHERE Nombre_proveedor = '{selection2.get()}'")
    temp=task.fetchone()
    if temp is not None:
        id_Proveedor=temp[0]
    else:
        id_Proveedor=0
    return id_Proveedor

def evaluarSiExiste(): #evalua si el registro a ingresar ya existe
    try:
        task.execute(f"SELECT 1 FROM Producto WHERE Nom_Producto = '{inputName.get()}' AND Modelo = '{inputModel.get()}' AND Color = '{inputColor.get()}'")
        data=task.fetchone()
        return data is None
    except ValueError:
        messagebox.showerror("Error","Ha ocurrido un error inesperado.")
    
def evaluarSiExisteConMismaGraduacion():
    booleano =False
    id_Producto=retornarId()
    try:
        task.execute(f"SELECT 1 FROM Graduaciones WHERE Id_Producto = {id_Producto}")
        temp=task.fetchone()
        if temp is not None:
            booleano=True
    except:
        pass
    #Me quedé aquí, no puedo evaluar porque no me deja hacer dos inserciones en la tabla graduaciones!!!!!!!!
    return booleano

def evaluarSolucionValue(): #pendiente
    booleano=False
    if(len(inputContenido.get()) < 15 and len(inputEmpleo.get()) < 45 and len(inputDetalles.get()) < 150):
        booleano=True
    return booleano

def evaluarGraduacionValue():
    booleano = False
    try:
        float(inputGraduacion.get())
        if(len(inputMica.get()) < 45 and len(inputTratamiento.get()) < 45):
            booleano=True
    except:
        pass
    return booleano 
        

def definirGraduacion(): #funciona solo para los productos que poseen graduacion 
    def insertarGraduacion():#inserta los valores de las graduaciones, color de mica, etc.
        try:
            if(evaluarSiExisteConMismaGraduacion()==False):
                if(evaluarGraduacionValue()):
                    task.execute(f"INSERT INTO Graduaciones(Id_Producto,Graduacion,Color_mica,Tratamiento_mica) VALUES({id_producto},'{inputGraduacion.get()}','{inputMica.get()}','{inputTratamiento.get()}')")
                    conexion.commit() #confirma la inserción a la base de datos
                    messagebox.showinfo("Datos guardados!","Los datos se han guardado con éxito.")
                    extra.destroy()
                    reset()
                else:
                    messagebox.showwarning("Datos incorrectos","Ingrese datos correctos en los campos.")
            else:
                messagebox.showwarning("Dato ya agregado","El producto ya está relacionado con una graduación") #se debe arreglar la relación de las tablas
        except ValueError:
            messagebox.showerror("Error","Ha ocurrido un error inesperado.")

    if(evaluarSiExiste()):
        task.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion,Foto_Producto) VALUES('{inputModel.get()}','{inputName.get()}',{id_Categoria},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{float(inputPrecio.get())},{float(inputCosto.get())},'{new_path}')")
        conexion.commit()
        task.execute(f"INSERT INTO Inventario(Id_Producto,Id_Proveedor,Stock_Producto,Fecha_Adquisicion) VALUES('{retornarId()}','{retornarIdProveedor()}','{stockInput.get()}','{dateInput.get()}')")
        conexion.commit()
    id_producto=retornarId()

    extra=tk.Toplevel(registro)
    extra.geometry("260x280")
    extra.title("Define la graduación")
    graduacion=tk.Label(extra,text="Gruaduación",font=("Calibri",12))
    graduacion.pack()
    global inputGraduacion
    inputGraduacion=tk.Entry(extra,width=20,justify='center')
    inputGraduacion.pack(pady=(5,20))
    colorMica=tk.Label(extra,text="Colo de mica",font=("Calibri",12))
    colorMica.pack()
    global inputMica
    inputMica=tk.Entry(extra,width=20,justify='center')
    inputMica.pack(pady=(5,20))
    tratamiento=tk.Label(extra,text="Tratamiento de mica",font=("Calibri",12))
    tratamiento.pack()
    global inputTratamiento
    inputTratamiento=tk.Entry(extra,width=20,justify='center')
    inputTratamiento.pack(pady=(5,20))
    guardar=tk.Button(extra,text="Guardar",width=10,font=("Calibri",12),command=insertarGraduacion)
    guardar.pack()

def insertarSolucion():
    def solucionMathEval():
        booleano =False
        id_Producto=retornarId()
        try:
            task.execute(f"SELECT 1 FROM Soluciones_aplicables WHERE Id_Producto = {id_Producto}")
            temp=task.fetchone()
            if temp is not None:
                booleano=True
        except:
            pass
        return booleano

    if(evaluarSolucionValue()):
        if(evaluarSiExiste()):
            try:
                task.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion,Foto_Producto) VALUES('{inputModel.get()}','{inputName.get()}',{id_Categoria},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{float(inputPrecio.get())},{float(inputCosto.get())},'{new_path}')")
                conexion.commit()
                task.execute(f"INSERT INTO Inventario(Id_Producto,Id_Proveedor,Stock_Producto,Fecha_Adquisicion) VALUES('{retornarId()}','{retornarIdProveedor()}','{stockInput.get()}','{dateInput.get()}')")
                conexion.commit()
            except ValueError:
                messagebox.showerror("Ha ocurrido un error inesperado")
        if(solucionMathEval()==False):
            task.execute(f"INSERT INTO Soluciones_aplicables(Id_Producto,Contenido_producto,Modo_empleo,Detalles) VALUES({retornarId()},'{inputContenido.get()}','{inputEmpleo.get()}','{inputDetalles.get()}')")
            conexion.commit()
            messagebox.showinfo("Inserción exitosa","Los datos se han insertado correctamente")
        else:
            messagebox.showerror("Error","El producto ya está asociado a un registro")
    else:
        messagebox.showerror("Error","Ingrese datos correctos en los campos")

def definirSolucion(): #terminar
    contenidoWindow=tk.Toplevel(registro)
    contenidoWindow.geometry("260x280")
    contenidoWindow.title("Ingresa el contenido del producto")
    contenido=tk.Label(contenidoWindow,text="Cantidad de contenido",font=("Calibri",12))
    contenido.pack()
    global inputContenido
    inputContenido=tk.Entry(contenidoWindow,width=20,justify='center')
    inputContenido.pack(pady=(5,20))
    modoEmpleo=tk.Label(contenidoWindow,text="Modo de empleo",font=("Calibri",12))
    modoEmpleo.pack()
    global inputEmpleo
    inputEmpleo=tk.Entry(contenidoWindow,width=20,justify='center')
    inputEmpleo.pack(pady=(5,20))
    detalles=tk.Label(contenidoWindow,text="Detalles a mencionar",font=("Calibri",12))
    detalles.pack()
    global inputDetalles
    inputDetalles=tk.Entry(contenidoWindow,width=40,justify='center')
    inputDetalles.pack(pady=(5,20))
    guardarContenido=tk.Button(contenidoWindow,text="Guardar",width=10,font=("Calibri",12),command=insertarSolucion)
    guardarContenido.pack()

def insertarRegistros(): #Inserta registros sencillos
    if(extra.get()==""): #si no posee ningún dato extra en el producto
        if(evaluarSiExiste()): #Evalua que el registro no exista si existe no tiene caso volver a agregarlo
            try:#intenta hacer la inserción
                task.execute(f"INSERT INTO Producto(Modelo,Nom_producto,Id_Categoria,Marca,Material,Color,Precio_venta,Costo_Adquisicion,Foto_Producto) VALUES('{inputModel.get()}','{inputName.get()}',{retornarIdCategoria()},'{inputMarca.get()}','{inputMaterial.get()}','{inputColor.get()}',{float(inputPrecio.get())},{float(inputCosto.get())},'{new_path}')")   
                conexion.commit()
                task.execute(f"INSERT INTO Inventario(Id_Producto,Id_Proveedor,Stock_Producto,Fecha_Adquisicion) VALUES('{retornarId()}','{retornarIdProveedor()}','{stockInput.get()}','{dateInput.get()}')")
                conexion.commit()
                messagebox.showinfo("Datos guardados!","Los datos se han guardado con éxito.")
                reset()
            except ValueError:#error de conexión o inserción por algún motivo
                    messagebox.showerror("Error","Ha ocurrido un error inesperado")#envia el mensaje de error
        else:
            messagebox.showinfo("Ya agregado","El registro ya existe.")
    elif(extra.get()=="graduacion"):
        definirGraduacion()
    elif(extra.get()=="liquido"):       #si necesita insertar datos de soluciones entraría aquí
        definirSolucion()

def evaluarRegistros(): #evalua las entradas de la ventana para producto
    flotante=False
    try:
        float(inputPrecio.get())
        float(inputCosto.get())
        int(stockInput.get()) ### Me quedé aquí ### 
        flotante=True
    except ValueError:
        pass
    task.execute(f"SELECT Id_Categoria FROM Categoria WHERE Nombre_Categoria = '{selection.get()}'")
    result=task.fetchone()
    if result is None:
        flotante=False
    else:
        global id_Categoria
        id_Categoria=result[0]
    task.execute(f"SELECT Id_Proveedor FROM Proveedor WHERE Nombre_proveedor = '{selection2.get()}'")
    result2=task.fetchone()
    if result2 is None:
        flotante=False
    else:
        flotante=True
    evaluateModel=(len(inputModel.get())<=45)
    evaluateName=(len(inputName.get())<=45)
    evaluateMarca=(re.match("^[a-zA-Z\s]+$",inputMarca.get()) and len(inputMarca.get())<=20)
    evaluateMaterial=(re.match("^[a-zA-Z\s]+$",inputMaterial.get()) and len(inputMaterial.get())<=10)
    evaluateColor=(re.match("^[a-zA-Z\s]+$",inputColor.get()) and len(inputColor.get())<=20)
    evaluarFecha=True if ("/" in dateInput.get() or "-" in dateInput.get() and re.match(r"^([0-9]{4})(-|/)([0-9]{1,2})(-|/)([0-9]{1,2})$",dateInput.get()) is not None) else False
    if(len(dateInput.get())==10):
        evaluarFecha=True
    else:
        evaluarFecha=False
        print("falso")
    if(evaluateModel and evaluateName and evaluateMarca and evaluateMaterial and evaluateColor and flotante and evaluarFecha):
        insertarRegistros()
    else:
        messagebox.showerror("Entradas incorrectas","Por favor, ingrese datos correctos.")

global new_path
def ingresarRegistro(event): #genera una ventana para ingresar datos en producto
    def take_photo():
        cap=cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('Presiona la tecla "s" para tomar una foto', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                timestr=time.strftime("%Y%m%d-%H%M%S")
                global new_path
                new_path = f"HTML/imagenes-productos/photo_{timestr}.jpg"
                cv2.imwrite(new_path, frame)
                new_path=new_path.replace("\\","/")
                break
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cap.release()
    def choose_photo():
        file_path=filedialog.askopenfilename(filetypes=[("Image files","*.jpg;*.png")])
        if file_path:
            global new_path
            path = f"HTML/imagenes-productos"
            file_name = os.path.basename(file_path)
            new_path = os.path.join(path, file_name)
            shutil.copy(file_path, new_path)

    global registro
    registro=tk.Toplevel(root)
    registro.geometry("680x460")
    registro.title("Agregar registro")
    #Modelo
    labelModel=tk.Label(registro,text="Modelo",font=("Calibri,14"),padx=20)
    labelModel.grid(row=0,column=0,sticky='w')
    global inputModel
    inputModel=tk.Entry(registro,width=50,justify='left')
    inputModel.grid(row=0,column=1,padx=10)
    
    #Nombre
    labelName=tk.Label(registro,text="Nombre del producto",font=("Calibri",14),padx=20)
    labelName.grid(row=1,column=0,sticky='w')
    global inputName
    inputName=tk.Entry(registro,width=50,justify='left')
    inputName.grid(row=1,column=1)

    #categoría
    options=[]
    try:
        task.execute("SELECT * FROM Categoria")
        temp1=task.fetchall()
        for op in temp1:
            options.append(op[1])
    except ValueError:
        pass
    global selection
    selection=tk.StringVar()
    selection.set("Seleccionar")
    if(len(options) != 0):
        menuCategory=tk.OptionMenu(registro,selection,*options) #modificar
        menuCategory.grid(row=2,column=1,sticky='w',padx=10)
    else:
        menuCategory=tk.OptionMenu(registro,selection,"") #modificar
        menuCategory.grid(row=2,column=1,sticky='w',padx=10)
    labelCategory=tk.Label(registro,text="Categoria",font=("Calibri",14),padx=20)
    labelCategory.grid(row=2,column=0,sticky='w')

    #Marca 
    marcaLabel=tk.Label(registro,text="Marca del producto",font=("Calibri",14),padx=20)
    marcaLabel.grid(row=3,column=0,sticky='w')
    global inputMarca
    inputMarca=tk.Entry(registro,width=50,justify='left')
    inputMarca.grid(row=3,column=1)

    #material
    materialLabel=tk.Label(registro,text="Material de fabricación",font=("Calibri",14),padx=20)
    materialLabel.grid(row=4,column=0,sticky='w')
    global inputMaterial
    inputMaterial=tk.Entry(registro,width=50,justify='left')
    inputMaterial.grid(row=4,column=1)

    #Color
    colorLabel=tk.Label(registro,text="Color del producto",font=("Calibri",14),padx=20)
    colorLabel.grid(row=5,column=0,sticky='w')
    global inputColor
    inputColor=tk.Entry(registro,width=50,justify='left')
    inputColor.grid(row=5,column=1)

    #Precio_Venta
    precioVentaLabel=tk.Label(registro,text="Precio de venta",font=("Calibri",14),padx=20)
    precioVentaLabel.grid(row=6,column=0,sticky='w')
    global inputPrecio
    inputPrecio=tk.Entry(registro,width=50,justify='left')
    inputPrecio.grid(row=6,column=1)

    #Costo de aquisición
    costoLabel=tk.Label(registro,text="Costo de adquisición",font=("Calibri",14),padx=20)
    costoLabel.grid(row=7,column=0,sticky='w')
    global inputCosto
    inputCosto=tk.Entry(registro,width=50,justify='left')
    inputCosto.grid(row=7,column=1)

    #Extras
    global extra
    extra=tk.StringVar()
    extra.set("")
    option0=tk.Radiobutton(registro,text="Ninguno",variable=extra,value="")
    option0.place(x=20,y=360)
    option1=tk.Radiobutton(registro,text="Posee graduación",variable=extra,value="graduacion")
    option1.place(x=180,y=360)
    option2=tk.Radiobutton(registro,text="Posee líquido",variable=extra,value="liquido")
    option2.place(x=360,y=360)

    #Foto del producto
    fotoLabel=tk.Label(registro,text="Fotografía del producto",font=("Calibri",14),padx=20)
    fotoLabel.grid(row=11,column=0,sticky='w')
    tomarFoto=tk.Button(registro,text="Tomar foto",width=10,font=("Calibri",14),command=take_photo)
    tomarFoto.place(x=350,y=320)
    elegirFoto=tk.Button(registro,text="Elegir foto",width=10,font=("Calibri",14),command=choose_photo)
    elegirFoto.place(x=550,y=320)

    #Agregar a inventario
    opciones=[]
    global selection2
    selection2=tk.StringVar()
    selection2.set("Seleccionar")
    proveedor=tk.Label(registro,text="Proveedor del producto",font=("Calibri",14),padx=20)
    proveedor.grid(row=8,column=0,sticky='w')
    try:
        task.execute("SELECT * FROM Proveedor")
        temp=task.fetchall()
        for op2 in temp:
            opciones.append(op2[1])
    except:
        pass
    if(len(opciones)!=0):
        menuProveedor=tk.OptionMenu(registro,selection2,*opciones) #modificar
        menuProveedor.grid(row=8,column=1,sticky='w',padx=10)
    else:
        menuProveedor=tk.OptionMenu(registro,selection2,"") #modificar
        menuProveedor.grid(row=8,column=1,sticky='w',padx=10)

    #stock
    global stockInput
    stock=tk.Label(registro,text="Cantidad de stock disponible",font=("Calibri",14),padx=20)
    stock.grid(row=9,column=0,sticky='w')
    stockInput=tk.Entry(registro,width=50,justify='left')
    stockInput.grid(row=9,column=1)

    #fecha de adquisición
    global dateInput
    date=tk.Label(registro,text="Fecha en la que se adquirió el producto",font=("Calibri",14),padx=20)
    date.grid(row=10,column=0,sticky='w')
    dateInput=tk.Entry(registro,width=50,justify='left')
    dateInput.insert(0,"yyyy/mm/dd")
    dateInput.grid(row=10,column=1)

    #Enviar
    send=tk.Button(registro,text="Guardar",width=10,font=("Calibri",14),command=evaluarRegistros)
    send.place(x=230,y=390)


#función para agregar proveedores
def addSeller(event):
    def resetValues():
        nameInput.delete(0,tk.END)
        nombreInput.delete(0,tk.END)
        pInput.delete(0,tk.END)
        mInput.delete(0,tk.END)
        addresInput.delete(0,tk.END)
        phoneInput.delete(0,tk.END)
        mailInput.delete(0,tk.END)
        webSiteInput.delete(0,tk.END)
    def returnValues():
        name=nameInput.get()
        nombre=nombreInput.get()
        paterno=pInput.get()
        materno=mInput.get()
        addres=addresInput.get()
        phone=phoneInput.get()
        mail=mailInput.get()
        webSite=webSiteInput.get()
        value(name,nombre,paterno,materno,addres,phone,mail,webSite)

    def value(name,nombre,paterno,materno,addres,phone,mail,webSite):
        if(len(name) <= 45 and name!="" and len(nombre) <= 45 and nombre!="" and len(paterno) <= 45 and paterno!="" and len(materno) <= 45 and len(addres) <= 100 and addres!="" and len(phone) == 10 and phone.isdigit() and len(mail) <= 70 and mail!="" and len(webSite) <= 200):
            try:
                task.execute(f"SELECT 1 FROM Proveedor WHERE Nombre_proveedor = '{name}' AND Sitio_web = '{webSite}'")
                temp=task.fetchone()
                if temp is not None:
                    result=True
                else:
                    result=False
            except ValueError:
                messagebox.showerror("Error","Ha ocurrido un error inesperado.")
            if(result==False):
                insertProveedor(name,nombre,paterno,materno,addres,phone,mail,webSite)
            else:
                messagebox.showwarning("Dato ya ingresado","El registro ya existe.")
        else:
            messagebox.showwarning("Datos incorrectos","Por favor, ingrese datos correctos en los campos")

    def insertProveedor(name,nombre,paterno,materno,addres,phone,mail,webSite):
        try:
            task.execute(f"INSERT INTO Proveedor(Nombre_proveedor,Nombre_representante,Paterno_representante,Materno_representante,Direccion,Telefono,Correo,Sitio_web) VALUES('{name}','{nombre}','{paterno}','{materno}','{addres}','{phone}','{mail}','{webSite}')")
            conexion.commit()
            messagebox.showinfo("Datos insertado con éxito!","Los datos han sido guardados exitosamente.")
            resetValues()
        except ValueError:
            messagebox.showerror("Error","Ha ocurrido un error inesperado.")

    seller=tk.Toplevel(root)
    seller.geometry("580x330")
    seller.title("Agregar proveedor")
    #me quedé aquí!!!!
    name=tk.Label(seller,text="Nombre del proveedor",font=("Calibri",12))
    name.grid(row=0,column=0,sticky='w',padx=(5,50),pady=4)
    nameInput=tk.Entry(seller,width=50,justify='left')
    nameInput.grid(row=0,column=1)

    nombre=tk.Label(seller,text="Nombre del representante",font=("Calibri",12))
    nombre.grid(row=1,column=0,sticky='w',padx=(5,50),pady=4)
    nombreInput=tk.Entry(seller,width=50,justify='left')
    nombreInput.grid(row=1,column=1)

    apellidoP=tk.Label(seller,text="Apellido paterno del representante",font=("Calibri",12))
    apellidoP.grid(row=2,column=0,sticky='w',padx=(5,20),pady=4)
    pInput=tk.Entry(seller,width=50,justify='left')
    pInput.grid(row=2,column=1)

    apellidoM=tk.Label(seller,text="Apellido materno del representante",font=("Calibri",12))
    apellidoM.grid(row=3,column=0,sticky='w',padx=(5,20),pady=4)
    mInput=tk.Entry(seller,width=50,justify='left')
    mInput.grid(row=3,column=1)

    addres=tk.Label(seller,text="Dirección",font=("Calibri",12))
    addres.grid(row=4,column=0,sticky='w',padx=(5,20),pady=4)
    addresInput=tk.Entry(seller,width=50,justify='left')
    addresInput.grid(row=4,column=1)

    phone=tk.Label(seller,text="Teléfono de contacto",font=("Calibri",12))
    phone.grid(row=5,column=0,sticky='w',padx=(5,20),pady=4)
    phoneInput=tk.Entry(seller,width=50,justify='left')
    phoneInput.grid(row=5,column=1)

    mail=tk.Label(seller,text="Correo de contacto",font=("Calibri",12))
    mail.grid(row=6,column=0,sticky='w',padx=(5,20),pady=4)
    mailInput=tk.Entry(seller,width=50,justify='left')
    mailInput.grid(row=6,column=1)

    webSite=tk.Label(seller,text="Sitio web de contacto",font=("Calibri",12))
    webSite.grid(row=7,column=0,sticky='w',padx=(5,20),pady=4)
    webSiteInput=tk.Entry(seller,width=50,justify='left')
    webSiteInput.grid(row=7,column=1)

    save=tk.Button(seller,text="Guardar",font=("Arial",12),width=10,command=returnValues)
    save.place(x=260,y=280)

def guardarEvento(evento):
    messagebox.showinfo("Funciona","El evento funcionó!")

def visualizarInv(): #Por el momento queda así  
    visualizacion=tk.Toplevel(root)
    visualizacion.geometry("950x400")
    visualizacion.config(bg="#D9E2F3")
    visualizacion.title("Productos en inventario")
    producto=ttk.Treeview(visualizacion,columns=('Id_Producto','Modelo','Nom_Producto','Categoria','Marca','Material','Color','Precio_De_Venta','Costo_De_Adquisición','Proveedor','Stock','Fecha_Adquisicion'),show='headings')
    producto.place(x=24,y=20,width=890,height=350)
    producto.heading('Id_Producto',text='Id_Producto')
    producto.heading('Modelo',text='Modelo')
    producto.heading('Nom_Producto',text='Nombre del producto')
    producto.heading('Categoria',text='Categoria')
    producto.heading('Marca',text='Marca')
    producto.heading('Material',text='Material')
    producto.heading('Color',text='Color')
    producto.heading('Precio_De_Venta',text='Precio de venta')
    producto.heading('Costo_De_Adquisición',text='Costo de adquisición')
    producto.heading('Proveedor',text='Proveedor')
    producto.heading('Stock',text='Existencia de producto')
    producto.heading('Fecha_Adquisicion',text='Fecha de aquisición')
    producto.column('Id_Producto',anchor='center')
    producto.column('Modelo',anchor='center')
    producto.column('Nom_Producto',anchor='center')
    producto.column('Categoria',anchor='center')
    producto.column('Marca',anchor='center')
    producto.column('Material',anchor='center')
    producto.column('Color',anchor='center')
    producto.column('Precio_De_Venta',anchor='center')
    producto.column('Costo_De_Adquisición',anchor='center')
    producto.column('Proveedor',anchor='center')
    producto.column('Stock',anchor='center')
    producto.column('Fecha_Adquisicion',anchor='center')
    scrolledBar=ttk.Scrollbar(visualizacion,orient='horizontal',command=producto.xview)
    scrolledBar.pack(side='bottom',fill='x',pady=5,padx=20)
    producto.configure(yscrollcommand=scrolledBar.set)
    task.execute("SELECT * FROM Producto")
    datos=task.fetchall()
    for dato in datos:
        insercion=list(dato)
        if dato is not None:
            try:
                task.execute(f"SELECT Nombre_Categoria FROM Categoria WHERE Id_Categoria = {dato[3]}")
                temp=task.fetchone()
                insercion[3]=temp
                task.execute(f"SELECT Id_Proveedor FROM Inventario WHERE Id_Producto = {dato[0]}")
                temp=task.fetchone()
                task.execute(f"SELECT Nombre_proveedor FROM Proveedor WHERE Id_Proveedor = {temp[0]}")
                temp=task.fetchone()
                insercion.append(temp[0])
                task.execute(f"SELECT Stock_Producto FROM Inventario WHERE Id_Producto = {dato[0]}")
                temp=task.fetchone()
                insercion.append(temp[0])
                task.execute(f"SELECT Fecha_Adquisicion FROM Inventario WHERE Id_Producto = {dato[0]}")
                temp=task.fetchone()
                insercion.append(temp[0])
            except:
                pass
        producto.insert('','end',values=insercion)

def visualizarProveedores():
    visualizacion=tk.Toplevel(root)
    visualizacion.geometry("950x400")
    visualizacion.config(bg="#D9E2F3")
    visualizacion.title("Proveedores")
    tabla=ttk.Treeview(visualizacion,columns=('Id_Proveedor','Nombre_Proveedor','Nombre_Representante','Paterno_Representante','Materno_Representante','Direccion','Telefono','Correo','Sitio_Web'),show='headings')
    tabla.place(x=24,y=20,width=890,height=350)
    tabla.heading('Id_Proveedor',text='Id del proveedor')
    tabla.heading('Nombre_Proveedor',text='Nombre de la empresa')
    tabla.heading('Nombre_Representante',text='Nombres del representante')
    tabla.heading('Paterno_Representante',text='Apellido paterno del representante')
    tabla.heading('Materno_Representante',text='Apellido materno del representante')
    tabla.heading('Direccion',text='Direccion de la empresa')
    tabla.heading('Telefono',text='Telefono de contacto')
    tabla.heading('Correo',text='Correo de contacto')
    tabla.heading('Sitio_Web',text='Página de contacto')
    tabla.column('Id_Proveedor',anchor='center')
    tabla.column('Nombre_Proveedor',anchor='center')
    tabla.column('Nombre_Representante',anchor='center')
    tabla.column('Paterno_Representante',anchor='center')
    tabla.column('Materno_Representante',anchor='center')
    tabla.column('Direccion',anchor='center')
    tabla.column('Telefono',anchor='center')
    tabla.column('Correo',anchor='center')
    tabla.column('Sitio_Web',anchor='center')
    scrolledBar=ttk.Scrollbar(visualizacion,orient='horizontal',command=tabla.xview)
    scrolledBar.pack(side='bottom',fill='x',pady=5,padx=20)
    tabla.configure(yscrollcommand=scrolledBar.set)
    try:
        task.execute("SELECT * FROM Proveedor")
        datos=task.fetchall()
        for dato in datos:
            tabla.insert('','end',values=dato)
    except:
        messagebox.showerror("Error en la consulta","Ha ocurrido un error inesperado")
    
def updateInv():
    def busquedas(*args):
        texto=busqueda.get()
        task.execute(f"SELECT Nom_Producto FROM Producto WHERE Nom_Producto LIKE '%{texto}%'")
        temp=task.fetchall()
        for i in produc.get_children():
            produc.delete(i)
        for data in temp:
            produc.insert('','end',values=data)
    def seleccion(event):
        selecc=produc.selection()
        if selecc:
            datos=produc.item(selecc,'values')[0]
            task.execute(f"SELECT * FROM Producto WHERE Nom_Producto = '{datos}'")
            temp=task.fetchone()
            modelo.delete(0,tk.END)
            modelo.insert(0,temp[1])
            nombre.delete(0,tk.END)
            nombre.insert(0,temp[2])
            marca.delete(0,tk.END)
            marca.insert(0,temp[4])
            material.delete(0,tk.END)
            material.insert(0,temp[5])
            color.delete(0,tk.END)
            color.insert(0,temp[6])
            precio.delete(0,tk.END)
            precio.insert(0,temp[7])
            task.execute(f"SELECT Nombre_Categoria FROM Categoria WHERE Id_Categoria = {temp[3]}")
            temp2=task.fetchone()
            categoria.set(temp2[0])
            task.execute(f"SELECT Stock_Producto FROM Inventario WHERE Id_Producto = {temp[0]}")
            temp3=task.fetchone()
            stock.delete(0,tk.END)
            stock.insert(0,temp3[0])
    def update():
        selecc=produc.selection()
        try:
            if selecc:
                dato=produc.item(selecc,'values')[0]
                task.execute(f"SELECT Id_Producto FROM Producto WHERE Nom_producto = '{dato}'")
                temp=task.fetchone()
                task.execute(f"SELECT Id_Categoria FROM Categoria WHERE Nombre_Categoria = '{categoria.get()}'")
                temp2=task.fetchone()
                task.execute(f"UPDATE Producto SET Modelo = '{modelo.get()}', Nom_producto = '{nombre.get()}', Marca = '{marca.get()}', Material = '{material.get()}', Color = '{color.get()}', Precio_venta = {float(precio.get())}, Id_Categoria = {temp2[0]} WHERE Id_Producto = {temp[0]}")
                task.execute(f"UPDATE Inventario SET Stock_Producto = {stock.get()} WHERE Id_Producto = {temp[0]}")
                conexion.commit()
                messagebox.showinfo("Guardado!","Los datos se han actualizado con éxito!")
                produc.delete(selecc[0])
                produc.insert('','end',values=nombre.get())
        except ValueError:
            messagebox.showerror("Error","Ha ocurrido un error inesperado")

    visualizacion=tk.Toplevel(root)
    visualizacion.geometry("950x600")
    visualizacion.config(bg="#D9E2F3")
    visualizacion.title("Inventario")
    textOne=tk.Label(visualizacion,text="Elija un producto",font=("Arial",16),justify='center',bg="#D9E2F3")
    textOne.pack(pady=(10,0),padx=(0,0))
    #Contenedor
    container=tk.Frame(visualizacion,width=940,height=540,bg="#D9E2F3")
    container.pack()
    container.grid_propagate(False)
    #Scroll text que contiene todos los productos
    produc=ttk.Treeview(container,columns=('Productos'),show='headings')
    produc.place(x=0,y=50,width=305,height=490)
    produc.heading('Productos',text='Productos')
    produc.column('Productos',anchor='center')
    produc.bind('<<TreeviewSelect>>',seleccion)
    try:
        task.execute("SELECT Nom_Producto FROM Producto")
        temp=task.fetchall()
        for data in temp:
            produc.insert('','end',values=data)
    except ValueError:
        messagebox.showerror("Error","Ha ocurrido un error inesperado")
    #Input de busqueda
    busqueda=tk.StringVar()
    busqueda.trace('w',busquedas)
    entrada=tk.Entry(container,width=23,justify='left',font=("Arial",18),textvariable=busqueda)
    entrada.grid(row=0,column=0,pady=(10,0))
    #datos a cambiar
    modelLabel=tk.Label(container,text="Modelo",font=("Calibri",14),justify='left',bg="#D9E2F3")
    modelLabel.grid(row=0,column=1,padx=(40,0),sticky='w')
    modelo=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    modelo.grid(row=1,column=1,pady=(2,0),padx=(40,0))
    nombreLabel=tk.Label(container,text="Nombre del producto",font=("Calibri",14),justify='left',bg="#D9E2F3")
    nombreLabel.grid(row=0,column=2,padx=(40,0),sticky='w')
    nombre=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    nombre.grid(row=1,column=2,pady=(2,0),padx=(40,0))
    marcaLabel=tk.Label(container,text="Marca del producto",font=("Calibri",14),justify='left',bg="#D9E2F3")
    marcaLabel.grid(row=2,column=1,padx=(40,0),pady=(40,0),sticky='w')
    marca=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    marca.grid(row=3,column=1,pady=(2,0),padx=(40,0))
    materialLabel=tk.Label(container,text="Material del producto",font=("Calibri",14),justify='left',bg="#D9E2F3")
    materialLabel.grid(row=2,column=2,padx=(40,0),pady=(40,0),sticky='w')
    material=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    material.grid(row=3,column=2,pady=(2,0),padx=(40,0))
    colorLabel=tk.Label(container,text="Color del producto",font=("Calibri",14),justify='left',bg="#D9E2F3")
    colorLabel.grid(row=4,column=1,padx=(40,0),pady=(40,0),sticky='w')
    color=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    color.grid(row=5,column=1,pady=(2,0),padx=(40,0))
    precioLabel=tk.Label(container,text="Precio del producto",font=("Calibri",14),justify='left',bg="#D9E2F3")
    precioLabel.grid(row=4,column=2,padx=(40,0),pady=(40,0),sticky='w')
    precio=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    precio.grid(row=5,column=2,pady=(2,0),padx=(40,0))
    try:
        datos=[]
        task.execute("SELECT Nombre_Categoria FROM Categoria")
        temp=task.fetchall()
        for dato in temp:
            datos.append(dato[0])
    except ValueError:
        pass
    categoria=tk.StringVar()
    categoria.set("Seleccionar")
    if (len(datos)!=0):
        categoriaMenu=tk.OptionMenu(container,categoria,*datos)
        categoriaMenu.place(x=340,y=300)
    else:
        categoriaMenu=tk.OptionMenu(container,categoria,"")
        categoriaMenu.place(x=340,y=300)
    stockLabel=tk.Label(container,text="Stock disponible",font=("Calibri",14),justify='left',bg="#D9E2F3")
    stockLabel.grid(row=6,column=2,padx=(40,0),pady=(40,0),sticky='w')
    stock=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    stock.grid(row=7,column=2,pady=(2,0),padx=(40,0))
    actualizar=tk.Button(container,text="Guardar",font=("Calibri",14),width=10,command=update)
    actualizar.place(x=580,y=430)
    
def updateProv():
    def seleccion(event):
        selec=prove.selection()
        if selec:
            datos=prove.item(selec,'values')[0]
            task.execute(f"SELECT * FROM Proveedor WHERE Nombre_proveedor = '{datos}'")
            temp=task.fetchone()
            nombre.delete(0,tk.END)
            nombre.insert(0,temp[1])
            nomRep.delete(0,tk.END)
            nomRep.insert(0,temp[2])
            paternoRep.delete(0,tk.END)
            paternoRep.insert(0,temp[3])
            maternoRep.delete(0,tk.END)
            maternoRep.insert(0,temp[4])
            direccion.delete(0,tk.END)
            direccion.insert(0,temp[5])
            phone.delete(0,tk.END)
            phone.insert(0,temp[6])
            mail.delete(0,tk.END)
            mail.insert(0,temp[7])
            web.delete(0,tk.END)
            web.insert(0,temp[8])

    def busquedas(*args):
        texto=busqueda.get()
        task.execute(f"SELECT Nombre_proveedor FROM Proveedor WHERE Nombre_proveedor LIKE '%{texto}%'")
        temp=task.fetchall()
        for i in prove.get_children():
            prove.delete(i)
        for data in temp:
            prove.insert('','end',values=data)

    def update():
        selec=prove.selection()
        try:
            if selec:
                dato=prove.item(selec,'values')[0]
                task.execute(f"SELECT Id_Proveedor FROM Proveedor WHERE Nombre_proveedor = '{dato}'")
                temp=task.fetchone()
                task.execute(f"UPDATE Proveedor SET Nombre_proveedor = '{nombre.get()}', Nombre_representante = '{nomRep.get()}', Paterno_representante = '{paternoRep.get()}', Materno_representante = '{maternoRep.get()}', Direccion = '{direccion.get()}', Telefono = '{phone.get()}', Correo = '{mail.get()}', Sitio_web = '{web.get()}' WHERE Nombre_proveedor = '{dato}'") 
                conexion.commit()
                messagebox.showinfo("Datos actualizados","Los datos se han guardado con éxito.")
                prove.delete(selec[0])
                prove.insert('','end',values=nombre.get())
        except ValueError:
            messagebox.showerror("Error","Ha ocurrido un error inesperado")

    visualizacion=tk.Toplevel(root)
    visualizacion.geometry("990x600")
    visualizacion.config(bg="#D9E2F3")
    visualizacion.title("Proveedor")
    proveedorLabel=tk.Label(visualizacion,text="Elige un proveedor",font=("Arial",14),justify='left',bg="#D9E2F3")
    proveedorLabel.grid(row=0,column=0,padx=10,pady=(10,0))
    container=tk.Frame(visualizacion,width=985,bg="#D9E2F3")
    container.place(x=6,y=50,height=590)
    prove=ttk.Treeview(container,columns=('Proveedores'),show='headings')
    prove.grid(row=1,column=0,pady=(10,0),sticky='nsew')
    prove.heading('Proveedores',text='Proveedores')
    prove.column('Proveedores',anchor='center')
    prove.bind('<<TreeviewSelect>>',seleccion)
    try:
        task.execute("SELECT Nombre_proveedor FROM Proveedor")
        temp=task.fetchall()
        for data in temp:
            prove.insert('','end',values=data)
    except ValueError:
        messagebox.showerror("Error","Ha ocurrido un error inesperado")
    busqueda=tk.StringVar()
    busqueda.trace('w',busquedas)
    entrada=tk.Entry(container,width=23,justify='left',font=("Arial",18),textvariable=busqueda)
    entrada.grid(row=0,column=0,pady=(10,0))
    #ME QUEDÉ AQUÍ!!!
    nombreLabel=tk.Label(container,text="Nombre del proveedor",font=("Calibri",14),justify='left',bg="#D9E2F3")
    nombreLabel.grid(row=0,column=1,padx=(40,0),sticky='w')
    nombre=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    nombre.grid(row=1,column=1,pady=(2,0),padx=(40,0),sticky='n')

    nomRepLabel=tk.Label(container,text="Nombre del representante",font=("Calibri",14),justify='left',bg="#D9E2F3")
    nomRepLabel.grid(row=0,column=2,padx=(40,0),sticky='w')
    nomRep=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    nomRep.grid(row=1,column=2,pady=(2,0),padx=(40,0),sticky='n')

    paternoRepLabel=tk.Label(container,text="Apellido paterno del representante",font=("Calibri",14),justify='left',bg="#D9E2F3")
    paternoRepLabel.place(x=345,y=130)
    paternoRep=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    paternoRep.place(x=345,y=170)

    maternoRepLabel=tk.Label(container,text="Apellido materno de representante",font=("Calibri",14),justify='left',bg="#D9E2F3")
    maternoRepLabel.place(x=660,y=130)
    maternoRep=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    maternoRep.place(x=660,y=170)

    direccionLabel=tk.Label(container,text="Dirección del proveedor",font=("Calibri",14),justify='left',bg="#D9E2F3")
    direccionLabel.place(x=345,y=250)
    direccion=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    direccion.place(x=345,y=290)

    phoneLabel=tk.Label(container,text="Telefono",font=("Calibri",14),justify='left',bg="#D9E2F3")
    phoneLabel.place(x=660,y=250)
    phone=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    phone.place(x=660,y=290)

    mailLabel=tk.Label(container,text="Correo",font=("Calibri",14),justify='left',bg="#D9E2F3")
    mailLabel.place(x=345,y=360)
    mail=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    mail.place(x=345,y=390)

    webLabel=tk.Label(container,text="Sitio web",font=("Calibri",14),justify='left',bg="#D9E2F3")
    webLabel.place(x=660,y=360)
    web=tk.Entry(container,width=30,font=("Calibri",13),justify='left')
    web.place(x=660,y=390)

    guardarBoton=tk.Button(container,text="Guardar",font=("Calibri",14),width=10,command=update)
    guardarBoton.place(x=585,y=460)

#establece la conexion a la base de datos y se crea la variable que ejecuta los comandos SQL
conexion=my.connect(host="localhost",user="root",passwd="",database="optilent")
task=conexion.cursor()



#se crea la ventana principal
root=tk.Tk()
root.title("Servicio de inventario")
root.geometry("920x650")
root.config(bg="#D9E2F3")

#Cabezal
head=tk.Frame(root,width=830,height=100,bg="#4472C4")
head.pack(pady=20)
head.propagate(False)
titular=tk.Label(head,text="OPTILENT",font=("Times",55),bg="#4472C4")
titular.pack()
imagen=Image.open("lentes.png")
imagen=imagen.resize((170,170))
photo=ImageTk.PhotoImage(imagen)
lentes=tk.Label(head,image=photo,bg="#4472C4")
lentes.place(x=60,y=-40)

#Bienvenido
welcome=tk.Label(root,text="¡Bienvenido!",font=("Arial",36),justify='center',bg="#D9E2F3")
welcome.pack()

#Main
main=tk.Frame(root,width=790,height=420,bg="#FFD966")
main.pack()
main.propagate(False)
#Texto de selección
cuadro1=tk.Frame(main,width=600,height=40,bg='white',highlightbackground="black",highlightthickness=2)
cuadro1.pack(pady=(30,0))
cuadro1.grid_propagate(False)
textInicio=tk.Label(cuadro1,text="SELECCIONE SU OPCION",font=("Arial",18),bg="white",justify='left')
textInicio.grid(row=0,column=0,sticky='w')
#contenido
cuadro2=tk.Frame(main,width=600,height=200,bg="white",highlightbackground="black",highlightthickness=2)
cuadro2.pack(pady=(20,0))
cuadro2.propagate(False)
#inventario
updateInventory=tk.Button(cuadro2,text="Actualizar datos en inventario",font=("Arial",16),justify='center',command=updateInv)
updateInventory.config(bg='White',relief='flat',width=600)
updateInventory.pack(pady=(5,0))
#Proveedores 
updateProveedor=tk.Button(cuadro2,text="Actualizar datos de proveedor",font=("Arial",16),justify='center',command=updateProv)
updateProveedor.config(bg='White',relief='flat',width=600)
updateProveedor.pack(pady=(5,0))
#visualizacion inventario
visualizarInventario=tk.Button(cuadro2,text="VISUALIZAR INVENTARIO",command=visualizarInv)
visualizarInventario.config(bg="white",relief='flat',width=600,font=("Arial",16))
visualizarInventario.pack(pady=(5,0))
#visualizar proveedores
visualizarProveedores=tk.Button(cuadro2,text="VISUALIZAR PROVEEDORES",command=visualizarProveedores)
visualizarProveedores.config(bg="white",relief='flat',width=600,font=("Arial",16))
visualizarProveedores.pack(pady=(5,0))
#boton de guardar
guardar=tk.Canvas(main,width=200,height=150,bg="#FFD966",highlightbackground="#FFD966")
guardar.place(x=60,y=290)
guardar.propagate(False)
labelG=tk.Label(guardar,text="AGREGAR REGISTRO",font=("Arial",12),justify='center',bg="#323f4f",fg="white")
labelG.place(x=20,y=45)
labelG.bind('<Button-1>',ingresarRegistro)
circle=guardar.create_oval(10,10,200,110,fill='#323f4f')

agregarProv=tk.Canvas(main,width=200,height=150,bg="#FFD966",highlightbackground="#FFD966")
agregarProv.place(x=520,y=290)
agregarProv.propagate(False)
labelA=tk.Label(agregarProv,text="AGREGAR PROVEEDOR",font=("Arial",11),justify='center',bg="#323f4f",fg='white')
labelA.place(x=15,y=45)
labelA.bind('<Button-1>',addSeller)
circle2=agregarProv.create_oval(10,10,200,110,fill='#323f4f')

root.mainloop()
