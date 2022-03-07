class Arreglo:
    def __init__(self) :
        self.aux=[]
        self.valores=[]
        self.tamaño=0;
        self.suma=0;
        self.Empezar()

    def Empezar(self):
        self.tamaño= (int) (input("ingrese el tamaño que desea "))   
        for i in range(self.tamaño):
            self.valores.append((int) (input()))

        for i in range(self.tamaño-1):
            for j in range((i+1),self.tamaño):
                self.suma=self.Suma(i,j)
                if self.suma ==0:
                    self.aux.append((j-i)+1)
                    break; 

        self.MetodoQuicSort()
        print(self.aux[0])            

    def MetodoQuicSort(self):
        pivote=0
        for i in range(1,len(self.aux)):
            j=i
            while j>0 and self.aux[j-1]>self.aux[j]:
                pivote =self.a[j-1]
                self.aux[j-1]=self.aux[j]
                self.aux[j]= pivote
                j-=1

    def Suma(self,i,j): 
        suma=0
        for x in range(i,(j+1)):
            suma += self.valores[x] 
        return suma



if __name__ == "__main__":
    Arreglo()