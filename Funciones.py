from Clases import Bombero
from Clases import Casilla

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")  
        print()
    print("\n")

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


def actualizarMapa(mapaAntiguo, posicion, bombero: Bombero):
    print("Pos mandada: ",posicion)
    filaB, columnaB = posicion

    for fila_idx, fila in enumerate(mapaAntiguo):
        for columna_idx, elemento in enumerate(fila):
            if(elemento == 5 and [filaB, columnaB] != [fila_idx,columna_idx]):
                mapaAntiguo[fila_idx][columna_idx] = 0
            elif(mapaAntiguo[filaB][columnaB] in (6,4,2,3)):
                nuevoBombero = asignarLitrosAguaBombero(mapaAntiguo[filaB][columnaB],bombero)
                mapaAntiguo[filaB][columnaB] = 5



    return mapaAntiguo, nuevoBombero



def asignarLitrosAguaBombero(casilla,bombero: Bombero):
    if (casilla == 3):
        bombero.setLitros(1)
        return bombero
    elif (casilla == 4):
        bombero.setLitros(2)
        return bombero
    elif(casilla == 2):
        bombero.quitarLitro()
        return bombero

    return bombero
