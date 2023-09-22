from collections import deque
from Clases import *
from Funciones import *

global posHidrante
global nodoPadreActual
global nodoCreado
#Esta función lee el mapa y me genera las casillas y el bombero
def cicloBombero(mapa):
    global nodoPadreActual
    casillas, bombero = crearPosiciones(mapa)
    print("Bombero: ", bombero.getPosiciones())
    nodoPadreActual = Nodo(bombero.getPosiciones(),None, None, 0, 1)

    algoritmoAmplitud(casillas,bombero,mapa)

def algoritmoAmplitud(casillas, bombero: Bombero, mapa):

    global posHidrante

    fila,columna = bombero.getPosiciones()
    tuplaPosicionBombero = [(fila, columna)]
    cola = deque(tuplaPosicionBombero)
    colaDespuesBusqueda = busqueda(cola, mapa)
    print("Buscando creación de nodos")

    posicionesFuegos = posicionesDelObjeto("Fuego", casillas)
    posicionesHidrantes = posicionesDelObjeto("Hidrante", casillas)
    posicionesCubetas = posicionesDelObjeto("Cubetas", casillas)

    if not bombero.getCubeta()[0]:
        posicionBalde = buscarCelda(mapa,colaDespuesBusqueda, posicionesCubetas)
        
        nuevoMapa, bomberoCambiado = actualizarMapa(mapa, posicionBalde, bombero)
        casillas, _ = crearPosiciones(nuevoMapa)
        print("MAPA")
        mostrarMapa(nuevoMapa)
        #algoritmoAmplitud(casillas,bomberoCambiado,mapa)

    elif(bombero.getLitros() > 0):
        posicionFuego = buscarCelda(mapa,colaDespuesBusqueda, posicionesFuegos)
        nuevoMapa, bomberoCambiado = actualizarMapa(mapa, posicionFuego, bombero)
        nuevoMapa[posHidrante[0]][posHidrante[1]] = 6
        casillas, _ = crearPosiciones(nuevoMapa)

        if(len(posicionesFuegos) == 0):
            print("FINALICÉ TODO")
            mostrarMapa(nuevoMapa)    
        else:
            algoritmoAmplitud(casillas,bomberoCambiado,nuevoMapa)
    else:
        posHidrante = posicionesHidrantes[0]
        posicionHidrante = buscarCelda(mapa,colaDespuesBusqueda, posicionesHidrantes)
        nuevoMapa, bomberoCambiado = actualizarMapa(mapa, posicionHidrante, bombero)
        casillas, _ = crearPosiciones(nuevoMapa)

        if(len(posicionesFuegos) == 0):
            print("FINALICÉ TODO")
            mostrarMapa(nuevoMapa)    
        else:
            algoritmoAmplitud(casillas,bomberoCambiado,nuevoMapa)

    return 0
    

#Esta funciones se pueden usar en todos los metodos

def busqueda(cola, mapa):
    elementosPrimero = obtenerElementosDelPrimero(cola)
    listaDisponible, listaCords = preguntarPorCasillasCercanas(elementosPrimero, mapa)
    resultadoFiltrado = filtrarDisponibles(listaDisponible, listaCords)
    agregarElementosCola(cola, resultadoFiltrado)

    return cola;

def preguntarPorCasillasCercanas(posicion, mapa):
    direcciones = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Izquierda, Abajo, Derecha, Arriba
    listaDisponible = []
    listaCords = []

    for direccion in direcciones:
        fila, columna = posicion[0] + direccion[0], posicion[1] + direccion[1]
        listaCords.append((fila, columna))

        if 0 <= fila < len(mapa) and 0 <= columna < len(mapa[0]):
            listaDisponible.append(mapa[fila][columna])
        else:
            listaDisponible.append(1)  # Valor para posiciones fuera de rango

    return listaDisponible, listaCords


def posicionDisponible(matriz, fila, columna):
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
        return matriz[fila][columna]
    else:
        return 1
    

def filtrarDisponibles(disponible,posiciones):
    print("\nDisponible: ", disponible)
    print("Posiciones: ", posiciones)
    resultado = []
    for tupla in posiciones:
        posicion = posiciones.index(tupla)  
        if disponible[posicion] in [0, 3, 2, 6]:
            resultado.append(tupla)
            crearNodo(posicion, posicion)
            

    return resultado


def crearNodo(posicion, direccion):
    global nodoCreado
    print("\n Dirección Elegida: ", direccion)
    movimiento= ""
    if(direccion == 0):
        movimiento = "←←←←←←"
    if(direccion == 1):
        movimiento = "↓↓↓↓↓↓"
    if(direccion == 2):
        movimiento = "→→→→→→"
    if(direccion == 3):
        movimiento = "↑↑↑↑↑↑"

    print("Movimiento: ", movimiento)
    
    # TODO: Tienes que hacer que el ultimo nodo creado sea igual al destino y así poder ir para arriba
    nodoCreado = Nodo(posicion,nodoPadreActual, movimiento, 0, 1)


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


def posicionesDelObjeto(objeto,casillas: Casilla):

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
    colaDespuesBusqueda = busqueda(posiciones, mapa)
    print("Cola: ", posiciones)

    if encuentraPosicion(posiciones,destino):
        posicionesActual = posiciones[0]
        return posicionesActual
    else:
        posicionesActual = buscarCelda(mapa, colaDespuesBusqueda,destino)
        return posicionesActual





