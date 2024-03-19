class Punto:
    def __init__(self, *coords):
        self._coords = list(coords)

    def traslacion(self, *deltas):
        for i in range(len(self._coords)):
            self._coords[i] += deltas[i]

    def __str__(self):
        if len(self._coords) == 2:
            return "X: {}; Y: {}".format(*self._coords)
        elif len(self._coords) == 3:
            return "X: {}; Y: {}; Z: {}".format(*self._coords)


class Punto2D(Punto):
    def __init__(self, x, y):
        super().__init__(x, y)


class Punto3D(Punto):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

# Crear un punto 2D
a = Punto2D(1, 2)
print("A =", a)

# Traslacion de punto 2D
a.traslacion(-1, -2)
print("A =", a)

# Crear y trasladar punto 2D
b = Punto2D(-3, 0)
b.traslacion(5, -1)
print("B =", b)

# Crear y trasladar punto 3D
c = Punto3D(4, 6, 8)
c.traslacion(1, 2, 3)
print("C =", c)