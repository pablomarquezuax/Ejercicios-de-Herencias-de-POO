class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion

class Ventana:
    def __init__(self, pared, superficie, proteccion=None):
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.pared = pared
        self.superficie = superficie
        self.proteccion = proteccion

    def __str__(self):
        return f"Ventana en la pared {self.pared.orientacion} con protección {self.proteccion}"

class ParedCortina(Pared):
    def __init__(self, orientacion, superficie_acristalada):
        super().__init__(orientacion)
        self.superficie_acristalada = superficie_acristalada

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        superficie_total = 0
        for pared in self.paredes:
            if isinstance(pared, ParedCortina):
                superficie_total += pared.superficie_acristalada
            else:
                for ventana in pared.ventanas:
                    superficie_total += ventana.superficie
        return superficie_total

# Instanciación de las paredes
pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = ParedCortina("SUR", 10)  # Usando ParedCortina para la pared sur
pared_este = Pared("ESTE")

# Instanciación de las ventanas
try:
    ventana_norte = Ventana(pared_norte, 0.5)
except TypeError as e:
    print("TypeError:", e)

try:
    ventana_norte = Ventana(pared_norte, 0.5, None)
except Exception as e:
    print("Exception:", e)

ventana_norte = Ventana(pared_norte, 0.5, "Persiana")  # Ventana con protección
ventana_oeste = Ventana(pared_oeste, 1, "Estor")
ventana_este = Ventana(pared_este, 1, "Cortina")

# Asociación de ventanas a las paredes
pared_norte.ventanas = [ventana_norte]
pared_oeste.ventanas = [ventana_oeste]
pared_este.ventanas = [ventana_este]

# Instanciación de la casa con las 4 paredes
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_acristalada())  # Salida: 4.5
