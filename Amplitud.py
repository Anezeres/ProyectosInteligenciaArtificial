from collections import deque
from Clases import *
from Funciones import *


def cicloBombero(mapa):

    casillas, bombero = crearPosiciones(mapa)
    print("Numero Casillas: ", len(casillas))

    algoritmoAmplitud(casillas,bombero,mapa)

def algoritmoAmplitud(casillas, bombero: Bombero, mapa):
    fila,columna = bombero.getPosiciones()
    tuplaPosicionBombero = [(fila, columna)]
    cola = deque(tuplaPosicionBombero)
    colaDespuesBusqueda = busqueda(cola, mapa)

    if(bombero.getLitros() == 0):
        posicionesCubetas = posicionesConCubetas("Cubetas", casillas)
        
        print("Posiciones con Cubetas: ",posicionesCubetas)
        
        posicionBalde = buscarCelda(mapa,colaDespuesBusqueda, posicionesCubetas)

        print("Posicion Actual: ", posicionBalde)

        nuevoMapa, bomberoCambiado = actualizarMapa(mapa, posicionBalde, bombero)

        print("Litros Bombero: ", bomberoCambiado.getLitros())

        imprimir_matriz(nuevoMapa)

        casillas, _ = crearPosiciones(nuevoMapa)
        algoritmoAmplitud(casillas,bomberoCambiado,mapa)

    else:
        posicionesHidrantes = posicionesConCubetas("Hidrante", casillas)
        print("Posiciones con Hidrantes: ",posicionesHidrantes)

    return 0
    

#Esta funciones se pueden usar en todos los metodos

def busqueda(cola, mapa):

    elementosPrimero = obtenerElementosDelPrimero(cola)

    print("Cola: ",cola)
    print("Casillas Cercanas: ", preguntarPorCasillasCercanas(elementosPrimero, mapa))

    listaDisponible, listaCords = preguntarPorCasillasCercanas(elementosPrimero, mapa)

    resultadoFiltrado = filtrarTuplas(listaDisponible, listaCords)

    print("Resultado Filtrado: ", resultadoFiltrado)

    agregarElementosCola(cola, resultadoFiltrado)

    print("Nueva Cola: ", cola)

    return cola;

def preguntarPorCasillasCercanas(posicion, mapa):
    arriba = posicionDisponible(mapa,posicion[0] - 1,posicion[1])
    abajo = posicionDisponible(mapa,posicion[0] + 1,posicion[1])
    izquierda = posicionDisponible(mapa,posicion[0],posicion[1] - 1)
    derecha = posicionDisponible(mapa,posicion[0],posicion[1] + 1)

    cordArriba = (posicion[0] - 1,posicion[1])
    cordAbajo = (posicion[0] + 1,posicion[1])
    cordizquierda = (posicion[0],posicion[1] - 1)
    cordDerecha = (posicion[0],posicion[1] + 1)

    listaDisponible = [izquierda, abajo, derecha, arriba]
    listaCords = [cordizquierda,cordAbajo,cordDerecha,cordArriba]

    return listaDisponible, listaCords;


def posicionDisponible(matriz, fila, columna):
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
        return matriz[fila][columna]
    else:
        return 1
    

def filtrarTuplas(disponible,posiciones):
    resultado = []
    for tupla in posiciones:
        posicion = posiciones.index(tupla)  
        if disponible[posicion] in [0, 3, 2, 6]:
            resultado.append(tupla)
    return resultado


def obtenerElementosDelPrimero(cola):
    if cola:
        primer_elemento = cola[0]
        if isinstance(primer_elemento, tuple) and len(primer_elemento) == 2:
            return list(primer_elemento)
    return None

def agregarElementosCola(cola, elementos):
    cola.popleft()
    elementos_agregados = set()
    for elemento in elementos:
        if elemento not in elementos_agregados:
            cola.append(elemento)
            elementos_agregados.add(elemento)


def posicionesConCubetas(objeto,casillas: Casilla):

    if(objeto == "Cubetas"):
        seleccionadas = [casilla for casilla in casillas if casilla.litros in (1, 2)]
    elif(objeto == "Hidrante"):
        seleccionadas = [casilla for casilla in casillas if casilla.tieneHidrante == True]
    elif(objeto == "Fuego"):
        seleccionadas = [casilla for casilla in casillas if casilla.tieneFuego == True]
    posiciones = []

    # Recorremos la lista de casillas y agregamos las posiciones a la lista
    for casilla in seleccionadas:
        posiciones.append((casilla.getPosiciones()))

    return posiciones


def encuentraPosicion(cola, destinos):
    if cola and cola[0] in destinos:
        return True
    return False


def buscarCelda(mapa, posiciones, destino):
    print("\n\n\nBuscando Balde") 
    colaDespuesBusqueda = busqueda(posiciones, mapa)

    if encuentraPosicion(posiciones,destino):
        print("\n\nEncontré Balde")
        print("Cola completa: ", posiciones)
        print("Destino: ", destino)

        posicionesActual = posiciones[0]
        return posicionesActual
    else: 
        print("Cola completa: ", posiciones)
        print("Destino: ", destino)
        posicionesActual = buscarCelda(mapa, colaDespuesBusqueda,destino)
        return posicionesActual





