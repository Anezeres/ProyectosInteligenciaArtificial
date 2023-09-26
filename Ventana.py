import tkinter as tk
from PIL import Image, ImageTk


global ventana

import random

def crearSprite(x,y):
    # Cargar la hoja de sprites completa
    imagen = Image.open("Sprites/sprites.png")

    # Coordenadas del área a recortar
    x_inicio = x * 16
    y_inicio = y * 16
    ancho_recorte =16
    alto_recorte = 16

    # Recortar la imagen
    imagen_recortada = imagen.crop((x_inicio, y_inicio, x_inicio + ancho_recorte, y_inicio + alto_recorte))

    # Convertir la imagen recortada a PhotoImage para Tkinter
    imagen_escala = imagen_recortada.resize((64, 64), Image.ANTIALIAS)
    imagen_tk = ImageTk.PhotoImage(imagen_escala)

    # Crear una etiqueta para mostrar la imagen
    return imagen_tk

def dibujar_imagenes_en_fila(lienzo, imagen, mapa):
    x = 0
    y = 0
    filas = 10
    columnas = 10
    sprite_size = 64
    

    for fila in range(filas):
        for columna in range(columnas):
            posX = x + columna * sprite_size
            posY = y + fila * sprite_size

            lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[0])

            if(mapa[fila][columna] == 1):
                imagen2 = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[1])
                lienzo.lift(imagen2)

            """ else:   
                lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[0]) """

            """ print("Fila: ", fila)
            print("Columna: ", columna) """


def crearSprites():

    sprites = []
    imagenPasto = crearSprite(19,8)
    imagenPiedra = crearSprite(17,4)

    sprites.append(imagenPasto)
    sprites.append(imagenPiedra)

    return sprites 


def generarVentana(mapa):
    global ventana
    ventana = tk.Tk()
    ventana.title("Mostrar Primer Sprite")

    sprites = crearSprites()

    lienzo = tk.Canvas(ventana, width=640, height=640)
    lienzo.pack()

    """ x_inicial = 0
    y_inicial = 100

    lienzo.create_image(x_inicial, y_inicial, anchor=tk.NW, image=imagen_tk) """

    dibujar_imagenes_en_fila(lienzo,sprites,mapa)

    # Ejecutar la ventana
    ventana.geometry("640x640")
    ventana.mainloop()