class Pila:
    def __init__(self):
        self._pila = []

    def Push(self, valor):
        self._pila.append(valor)

    def Empty(self):
        return len(self._pila) == 0

    def Pop(self):
        return self._pila.pop()

    def Peek(self):
        if len(self._pila) > 0:
            return self._pila[len(self._pila)-1]
        else:
            return 0


class Convertir:
    def __init__(self):
        self._Pila = Pila()
        self._list_salida = []
        self.Ingresar_expresion()

    def Ingresar_expresion(self):
        aux = ""
        self.lista = []
        valor = input()
        valor += 'ñ'
        for i in valor:
            if i.isnumeric():
                aux += i
            else:
                if aux != '':
                    self.lista.append(aux)
                aux = ''
                if i != " " and i != 'ñ':
                    self.lista.append(i)
        self.posfija()

    def posfija(self):
        contador = 0
        postfija = ""
        while len(self.lista) != 0:
            if self.lista[contador].isnumeric():
                self._list_salida.append(self.lista.pop(contador))
            elif self.lista[contador] == "(":
                self._Pila.Push(self.lista.pop(contador))
            elif self.lista[contador] == ")":
                while self._Pila.Empty() == False and self._Pila.Peek() != "(":
                    self._list_salida.append(self._Pila.Pop())
                if self._Pila.Peek() == "(":
                    self._Pila.Pop()
                self.lista.pop(contador)
            elif self.lista[contador] != "(" and self.lista[contador] != ")":
                while self._Pila.Empty() == False and self.comparar(self._Pila.Peek(), self.lista[contador]):
                    self._list_salida.append(self._Pila.Pop())
                self._Pila.Push(self.lista.pop(contador))
        while self._Pila.Empty() == False:
            self._list_salida.append(self._Pila.Pop())
        for i in self._list_salida:
            postfija += i
        print(postfija)

    def comparar(self, valor1, valor2):
        if self.infijo(valor1) >= self.infijo(valor2):
            return True
        else:
            return False

    def infijo(self, i):
        if(i == '^'):
            prioridadop = 4
            return prioridadop
        elif(i == '*'):
            prioridadop = 2
            return prioridadop
        elif(i == '/'):
            prioridadop = 2
            return prioridadop
        elif(i == '+'):
            prioridadop = 1
            return prioridadop
        elif(i == '-'):
            prioridadop = 1
            return prioridadop
        elif(i == '('):
            prioridadop = 0
            return prioridadop


if __name__ == "__main__":
    Convertir()
