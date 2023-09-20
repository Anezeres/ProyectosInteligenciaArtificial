from Clases import Casilla
from Clases import Bombero
from Amplitud import *

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")  
        print()
    print("\n")



def cicloBombero(mapa):

    casillas, bombero = crearPosiciones(mapa)
    print("Numero Casillas: ", len(casillas))

    algoritmoAmplitud(casillas,bombero,mapa)

    #casillas[0].imprimirAtributos()
    #bombero.imprimirPosicion()
    #posicionRaton = [fila, columna]
    

def crearPosiciones(matriz):
    listaObjetos = []
    bombero =0
    for fila, lista in enumerate(matriz):
        for columna, elemento in enumerate(lista):
            objetoActual = crearObjetos(elemento,fila, columna)[0]

            if elemento == 5:
                bombero = Bombero(0, (fila, columna))
                print("\nPosición del Bombero: ")
                print("Fila: ", fila, " Columna: ", columna, "\n")

            listaObjetos.append(objetoActual)

    return(listaObjetos, bombero)


#tieneHidrante, tieneFuego, solido litros, posición
def crearObjetos(tipoCasilla, fila, columna):
    configuraciones = {
        0: (False, False, False, 0, [fila, columna]),
        1: (False, False, True, 0, [fila, columna]),
        2: (False, True, False, 0, [fila, columna]),
        3: (False, False, False, 1, [fila, columna]),
        4: (False, False, False, 2, [fila, columna]),
        5: (False, False, False, 0, [fila, columna]),
        6: (True, False, False, 0, [fila, columna])
    }

    listaDePosiciones = []
    bombero = 0

    if tipoCasilla in configuraciones:
        argumentosCasilla = configuraciones[tipoCasilla]
        casilla = Casilla(*argumentosCasilla)
        listaDePosiciones.append(casilla)
        
        

        print(argumentosCasilla)
    return listaDePosiciones;

