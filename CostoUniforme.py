from collections import deque
from Clases import *
from Funciones import *

global posHidrante
global nodoPadreActual
global nodoCreado
global nodoDestino
global listaNodos
global listaMovimientosCU

def getListaMovimientos():
    return listaMovimientosCU

listaMovimientosCU = []
#Esta función lee el mapa y me genera las casillas y el bombero
def cicloBombero(mapa):
    global nodoPadreActual
    global listaNodos

    casillas, bombero = crearPosiciones(mapa)
    reiniciarListaNodos(bombero)

    algoritmoCU(casillas,bombero,mapa)


def algoritmoCU(casillas, bombero: Bombero, mapa):

    global posHidrante
    global nodoDestino
    global listaNodos
    global nodoPadreActual
    global listaMovimientosAmplitud

    if(len(listaNodos) > 1):
        listaNodos = []

    fila,columna = bombero.getPosiciones()
    tuplaPosicionBombero = [(fila, columna)]
    cola = deque(tuplaPosicionBombero)
    #colaDespuesBusqueda = busqueda(cola, mapa)

    posicionesFuegos = posicionesDelObjeto("Fuego", casillas)
    posicionesHidrantes = posicionesDelObjeto("Hidrante", casillas)
    posicionesCubetas = posicionesDelObjeto("Cubetas", casillas)

    if not bombero.getCubeta()[0]:
        print("No tiene Cubeta")


    elif(bombero.getLitros() > 0):
        print("Tiene Litros")
    else:
        print("Busca Hidrante")


    return 0

def reiniciarListaNodos(bomberoCambiado: Bombero):
    global listaNodos
    listaNodos = []
    nodoPadreActual = Nodo(bomberoCambiado.getPosiciones(),None, None, 0, 1)
    listaNodos.append(nodoPadreActual)