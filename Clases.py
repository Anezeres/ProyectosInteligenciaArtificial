class Casilla:
    def __init__(self, tieneHidrante, tieneFuego, solido, litros, posicion):
        self.tieneHidrante = tieneHidrante
        self.tieneFuego = tieneFuego
        self.solido = solido
        self.litros = litros
        self.posicion = posicion

    def imprimirAtributos(self):
        print("Tiene Hidrante:", self.tieneHidrante)
        print("Tiene Fuego:", self.tieneFuego)
        print("Es Sólido:", self.solido)
        print("Litros:", self.litros)
        print("Posición:", self.posicion)

    def getPosiciones(self):
        fila,columna = self.posicion
        return fila,columna;


class Bombero:
    def __init__(self, litrosCargados, posicion):
        self.litrosCargados = litrosCargados
        self.posicion = posicion

    def apagarFuego(self):
        if self.litrosCargados > 0:
            self.litrosCargados -= 1

    def imprimirPosicion(self):
        x, y = self.posicion
        print(f"Posición X: {x}, Posición Y: {y}")

    def getPosiciones(self):
        fila,columna = self.posicion
        return fila,columna;

    def setLitros(self, cantidad):
        self.litrosCargados = cantidad

    def getLitros(self):
        return self.litrosCargados

    def quitarLitro(self):
        if self.litros == 0:
            print("Debe buscar más Agua")
        else:
            self.litros -= 1

