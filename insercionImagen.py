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

def choose_photo():
        file_path=filedialog.askopenfilename(filetypes=[("Image files","*.jpg;*.png")])
        if file_path:
            global new_path
            path = f"HTML\\imagenes-productos"
            # path = f"C:\\Users\\alexc\\Desktop\\Formularios"
            file_name = os.path.basename(file_path)
            new_path = os.path.join(path, file_name)
            shutil.copy(file_path, new_path)

root=tk.Tk()
root.title("Servicio de inventario")
root.geometry("920x650")
root.config(bg="#D9E2F3")

elegirFoto=tk.Button(root,text="Elegir foto",width=10,font=("Calibri",14),command=choose_photo)
elegirFoto.place(x=550,y=320)

root.mainloop()
