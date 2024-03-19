class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        super().__init__(a)  # Llama al constructor de la clase A para inicializar el atributo a
        self.b = b

class C(A):
    def __init__(self, a, c):
        super().__init__(a)  # Llama al constructor de la clase A para inicializar el atributo a
        self.c = c

class D(B, C):
    def __init__(self, a, b, c):
        super().__init__(a, b)  # Llama al constructor de la clase B para inicializar los atributos a y b
        C.__init__(self, a, c)  # Llama al constructor de la clase C para inicializar los atributos a y c

# Instancia de la clase D con los valores 1, 2 y 3 para los atributos a, b y c respectivamente
d = D(1, 2, 3)

# Comprobación de la herencia
print(isinstance(d, A), isinstance(d, B), isinstance(d, C)) 

# Impresión de los valores de los atributos a, b y c
print(d.a, d.b, d.c)
