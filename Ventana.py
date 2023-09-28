import tkinter as tk
from PIL import Image, ImageTk
from Amplitud import *
import time


global ventana
global soldier
global lienzo
global mapa
global listaMovimientos
global listaObjetos


listaObjetos = []


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

def dibujarSprites(imagen):
    global soldier
    global lienzo
    global mapa

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
                piedra = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[1])
                lienzo.lift(piedra)
            elif(mapa[fila][columna] == 2):
                orco = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[2])
                lienzo.lift(orco)
                agregarObjetoLista(fila,columna,orco)
            elif(mapa[fila][columna] == 6):
                potion = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[3])
                lienzo.lift(potion)
            elif(mapa[fila][columna] == 5):
                soldier = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[4])
                lienzo.lift(soldier)
            elif(mapa[fila][columna] == 3):
                sword = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[5])
                lienzo.lift(sword)
                agregarObjetoLista(fila,columna,sword)
            elif(mapa[fila][columna] == 4):
                superSword = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[6])
                lienzo.lift(superSword)
                agregarObjetoLista(fila,columna,superSword)

def agregarObjetoLista(fila,columna,objeto):
    global listaObjetos

    listaObjetos.append([fila,columna,objeto])

def crearSprites():

    orcoPng = Image.open("Sprites/Orco.png")
    soldierPng = Image.open("Sprites/Soldier.png")
    potionPng = Image.open("Sprites/Potion.png")
    swordPng = Image.open("Sprites/Sword.png")
    superSwordPng = Image.open("Sprites/SuperSword.png")
    potionGrande = potionPng.resize((64, 64), Image.ANTIALIAS)
    soldierGrande = soldierPng.resize((41,64), Image.ANTIALIAS)
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

def moverSoldado(y, direccion):
    global lienzo
    global soldier
    global ventana
    
    lienzo.lift(soldier)

    if(direccion == "Abajo"):
        print("Movimiento: ", direccion)
        lienzo.move(soldier, 0, 64)
    elif(direccion == "Arriba"):
        print("Movimiento: ", direccion)
        lienzo.move(soldier, 0, -64)
    elif(direccion == "Derecha"):
        print("Movimiento: ", direccion)
        lienzo.move(soldier, 64, 0)
    elif(direccion == "Izquierda"):
        print("Movimiento: ", direccion)
        lienzo.move(soldier, -64, 0)

    ventana.update()

    return 0

    

def generarVentana(mapaCompleto):
    global lienzo
    global ventana
    global mapa
    #TODO Ahora hay que hacer que cuando le de click al boton el soldado empiece a moverse por el mapa

    mapa = mapaCompleto

    ventana = tk.Tk()
    ventana.title("Mostrar Primer Sprite")

    sprites = crearSprites()

    lienzo = tk.Canvas(ventana, width=640, height=640)
    lienzo.pack()

    dibujarSprites(sprites)

    boton = tk.Button(ventana, text="Botón", command=lambda: generarMovimientosAmplitud())
    boton.place(x=100, y=150)


    #moverSoldado(lienzo)

    # Ejecutar la ventana
    ventana.geometry("640x640")
    ventana.mainloop()

def identificarMovimientosCompletos():
    global listaMovimientos

    for lista_de_movimientos in listaMovimientos:

        for i in range(1, len(lista_de_movimientos)):
            fila_anterior, columna_anterior = lista_de_movimientos[i - 1]
            fila_actual, columna_actual = lista_de_movimientos[i]

            # Comparamos las filas y columnas para determinar la dirección
            if fila_anterior < fila_actual:
                direccion = "Abajo"
            elif fila_anterior > fila_actual:
                direccion = "Arriba"
            elif columna_anterior < columna_actual:
                direccion = "Derecha"
            elif columna_anterior > columna_actual:
                direccion = "Izquierda"

            
            moverSoldado(0, direccion)
            eliminarObjeto(fila_actual, columna_actual)
            time.sleep(1)

def generarMovimientosAmplitud():
    global listaMovimientos
    cicloBombero(mapa)
    listaMovimientos = getListaMovimientos()
    print("Lista movimientos: ", listaMovimientos)
    identificarMovimientosCompletos()


def eliminarObjeto(fila, columna):
    global listaObjetos
    global lienzo

    for sublista in listaObjetos:
        if sublista[0] == fila and sublista[1] == columna:
            lienzo.delete(sublista[2])


