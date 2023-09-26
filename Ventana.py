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
            elif(mapa[fila][columna] == 2):
                imagen2 = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[2])
                lienzo.lift(imagen2)

            elif(mapa[fila][columna] == 6):
                imagen2 = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[3])
                lienzo.lift(imagen2)
            elif(mapa[fila][columna] == 5):
                imagen2 = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[4])
                lienzo.lift(imagen2)
            elif(mapa[fila][columna] == 3):
                imagen2 = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[5])
                lienzo.lift(imagen2)
            elif(mapa[fila][columna] == 4):
                imagen2 = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[6])
                lienzo.lift(imagen2)

            """ else:   
                lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[0]) """

            """ print("Fila: ", fila)
            print("Columna: ", columna) """


def crearSprites():

    orcoPng = Image.open("Sprites/Orco.png")
    soldierPng = Image.open("Sprites/Soldier.png")
    potionPng = Image.open("Sprites/Potion.png")
    swordPng = Image.open("Sprites/Sword.png")
    superSwordPng = Image.open("Sprites/SuperSword.png")
    potionGrande = potionPng.resize((64, 64), Image.ANTIALIAS)
    soldierGrande = soldierPng.resize((39,62), Image.ANTIALIAS)
    swordGrande = swordPng.resize((64,64), Image.ANTIALIAS)
    superSwordGrande = superSwordPng.resize((64,64), Image.ANTIALIAS)

    sprites = []
    imagenPasto = crearSprite(19,8)
    imagenPiedra = crearSprite(17,4)
    imagenFuego = crearSprite(0,12)
    
    orco = ImageTk.PhotoImage(orcoPng)
    soldier = ImageTk.PhotoImage(soldierGrande)
    potion = ImageTk.PhotoImage(potionGrande)
    sword = ImageTk.PhotoImage(swordGrande)
    superSword = ImageTk.PhotoImage(superSwordGrande)

    sprites.append(imagenPasto)
    sprites.append(imagenPiedra)
    sprites.append(orco)
    sprites.append(potion)
    sprites.append(soldier)
    sprites.append(sword)
    sprites.append(superSword)
    #sprites.append(imagenFuego)

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