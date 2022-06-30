import tkinter
from tkinter import PhotoImage
from PIL import Image,ImageTk
from functools import partial
ventana = tkinter.Tk()

img = Image.open('river.png')
img = img.resize((50,60), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

img1 = Image.open("boca.png")
img1 = img1.resize((50, 60), Image.Resampling.LANCZOS)
img1 = ImageTk.PhotoImage(img1)

def boton_apretado(col, fila):
    global x
    if x:
        imagen = img
    else:
        imagen = img1
    tabla_botones[col][fila].config(image=imagen, height=63, width=65)
    x = not x

tabla_botones =[]
x = True
for i in range(3):
    fila_botones = []    
    for j in range(3):
        b = tkinter.Button(ventana,  command=partial(boton_apretado, i, j), height=4, width=5)
        b.grid(row=i, column=j)
        fila_botones.append(b)
    tabla_botones.append(fila_botones)

print(tabla_botones)
ventana.mainloop()