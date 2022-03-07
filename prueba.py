import time;

class prueba:
    def __init__(self):
        self.lista=[1,2,3,4,5,6,7,8,9,10]
        self.metodo()

    def metodo (self):
        aux=self.lista[:6]
        aux.pop()
        print("prueba",aux,self.lista)


if __name__ == "__main__":
    prueba()