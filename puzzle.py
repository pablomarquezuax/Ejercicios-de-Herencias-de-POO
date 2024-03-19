class Base:
    
    def __init__(self):#constructor
        self.a = "a" #incizaliza los atributos a, b, c
        self.b = "b"
        self.c = "c"
    
    def A(self): #metodo A que imprime el valor de self.a
        print(self.a)

    def B(self): #metodo B que imprime el valor de self.b
        print(self.b)

    def C(self):  #metodo C que imprime el valor de self.c
        print(self.c)


class Derivada(Base): #clase que hereda de Base

    def __init__(self): #constructor
        self.a = "aa" #establece un valor
        super().__init__() #llama al constructir heredado de clase Base
        self.c = "cc" #establece otro valor
    

    def A(self): #metodo A que imprime el valor de self.a
        print(self.a)


    def B(self):
        self.b = "bb" # Modifica el valor de self.b
        super().B() #llama el metodo B heredado de la clase Base
        print(self.b)


def main():
    base = Base()#crea instancias
    derivada = Derivada()

    #llama a cada método de la clase Base y Derivada
    base.A()            #sale "a"
    derivada.A()        #sale "aa"

    print()

    base.B()             #sale "b"
    derivada.B()         #sale "bb" dos veces

    base.C()             #sale "c"
    derivada.C()         #sale "cc" dosveces

    derivada = base #asigna la instancia base a la variable derivada

    #llama al método C de la clase Derivada (que ahora apunta a la instancia base)
    derivada.C()         #sale "c"

if __name__ == "__main__":
    main()
