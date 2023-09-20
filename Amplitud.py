from collections import deque

def algoritmoAmplitud(casillas, bombero, mapa):
    fila,columna = bombero.getPosiciones()
    tuplaPosicionBombero = [(fila, columna)]
    cola = deque(tuplaPosicionBombero)

    colaDespuesBusqueda = busqueda(cola, mapa)
    posicionesCubetas = posicionesConCubetas(casillas)
    
    print("Posiciones con Cubetas: ",posicionesCubetas)
    
    buscarBalde(mapa,colaDespuesBusqueda, posicionesCubetas)

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
        if disponible[posicion] == 0:
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


def posicionesConCubetas(casillas):
    seleccionadas = [casilla for casilla in casillas if casilla.litros in (1, 2)]

    posiciones = []

    # Recorremos la lista de casillas y agregamos las posiciones a la lista
    for casilla in seleccionadas:
        posiciones.append((casilla.getPosiciones()))

    return posiciones


def encuentraPosicion(cola, destinos):
    if cola and cola[0] in destinos:
        return True
    return False


def buscarBalde(mapa, posiciones, destino):


    #while not encuentraPosicion(posiciones,destino):
        colaDespuesBusqueda = busqueda(posiciones, mapa)

        if not encuentraPosicion(posiciones,destino):
            print("Encontré Balde")
            print("Cola completa: ", posiciones)
        else:
            buscarBalde(mapa, colaDespuesBusqueda, destino)
        