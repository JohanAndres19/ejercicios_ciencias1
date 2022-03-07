class Cola:
    def __init__(self):
        self.cola = []

    def Offer(self, valor):
        if len(self.cola) == 0:
            self.cola.append(valor)
        else:
            posicion = (len(self.cola))
            while valor.CompareTo(self.cola[posicion-1]) < 0 and posicion > 0:
                posicion -= 1
            if posicion == (len(self.cola)):
                self.cola.append(valor)
            else:
                self.cola.insert(posicion, valor)

    def Empty(self):
        return len(self.cola) == 0

    def Poll(self):
        if len(self.cola) != 0:
            return self.cola.pop(0).ToString()
        else:
            return None

    def Peek(self, posicion=None):
        if len(self.cola) != 0 and posicion == None:
            return self.cola[0]
        elif len(self.cola) != 0:
            return self.cola[posicion]
        else:
            return None



class Persona:
    def __init__(self, nombre, turno, edad):
        self._nombre = nombre
        self._turno = turno
        self._edad = edad

    def CompareTo(self, Persona):
        if self.GetEdad() >= 60 and Persona.GetEdad() < 60:
            return -10
        elif self.GetEdad() < 60 and Persona.GetEdad() >= 60:
            return 10
        else:
            return self.GetTurno()-Persona.GetTurno()

    def ToString(self):
        return self._nombre+" "+str(self._turno)+" "+str(self._edad)

    def GetEdad(self):
        return self._edad

    def GetTurno(self):
        return self._turno


class Fila:
    def __init__(self):
        self.cola = Cola()
        self.AgregarAlaCola()
        self.ImprimirLista()

    def AgregarAlaCola(self):
        self.cola.Offer(Persona("johan", 2, 19))
        self.cola.Offer(Persona("kevin", 6, 60))
        self.cola.Offer(Persona("jonathan", 3, 22))
        self.cola.Offer(Persona("jaime", 10, 79))
        self.cola.Offer(Persona("jorge", 9, 80))
        self.cola.Offer(Persona("maria", 4, 33))
        self.cola.Offer(Persona("valentina", 5, 23))
        self.cola.Offer(Persona("rosmery", 7, 33))

    def ImprimirLista(self):
        while self.cola.Empty() == False:
            print(self.cola.Poll())


if __name__ == "__main__":
    Fila()
