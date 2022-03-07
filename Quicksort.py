
class Quicksort():
    def __init__(self):
        self.numeros=[5, 23, 7, 2, 19, 17, 11, 67, 113, 3]
        self.numeros1=[2, 5, 3, 61, 12, 20, 30, 10, 2020, 9, 13]
        self.numeros2 = [6, 4, 17, 5, 12,2,9,19,7,1]
        self.numeros3=[50,20,15,10,70,40,90,100,80,60]
        self.numeros4=[3,15,7,5,13,8]
        self.numeros5=[50,20,15,10,70,40,90,100,80,60,6, 4, 17, 5, 12,2,9,19,7,1]
        self.aux1=0
        self.aux2=0
        self.aux3=True
        self.pilaI=[]
        self.pivotes=[]
        self.Organizado=[]
        self.MetodoQuickSort(self.numeros3,0,(len(self.numeros3)-1))
        print("ccccccc",self.numeros3)
        print("ddddddd",self.pivotes)
        

    def MetodoQuickSort(self,array,i,j):
        if len(array)>1:
          pivote=array[i]
          self.pivotes.append(pivote)
          self.derIzquier(array,i,j,pivote) 
          self.pilaI.append(array[:array.index(pivote)])
          self.Organizado.append(array)
          print(array)
          """
          self.Arr
          
          """
          self.MetodoQuickSort(array[self.GetAux2()+1:len(array)],0,len(array[self.GetAux2()+1:len(array)])-1) 
          print(self.pilaI)
        
       
    def izqDerecha(self,array,i,j,pivote):
        if i!=j:
            if pivote<array[i]:
               array[j] = array[i]
               j-=1
               self.derIzquier(array,i,j,pivote)
            else:
               i+=1
               self.izqDerecha(array,i,j,pivote) 
        else:
           array[i]=pivote
           self.SetAux2(i) 


    def derIzquier(self,array,i,j,pivote):
        if i!=j:
            if pivote>array[j]:
               array[i] = array[j]
               i+=1
               self.izqDerecha(array,i,j,pivote)
            else:
               j-=1
               self.derIzquier(array,i,j,pivote) 
        else:
           array[i]=pivote
           self.SetAux2(i)

    
    def ArregloIzquierda(self,array,i,j):
        """
        """        
        pivote=array[i]
        if self.GetAux2()!=0:
         self.derIzquier(array,i,j,pivote)
        if self.GetAux2()== 0:
          print("valor de i y j",i,j)  
          self.MetodoQuickSort(array,i,j)   
        else:
          pass   


    def ArregloDerecha(self,array,i,j):
        pivote=array[i]
        if self.GetAux2()!=(len(array)-1):
         self.derIzquier(array,i,j,pivote)
        if self.GetAux2()==(len(array)-1):
            self.MetodoQuickSort(array,i,j)
        else:
         pass
        print("valor de aux2 ",self.GetAux2()) 
    
  
  
    def GetAux1(self):
        return self.aux1

    def GetAux2(self):
        return self.aux2

    def GetAux3(self):
        return self.aux3    

    def SetAux1(self,aux1):
        self.aux1=aux1

    def SetAux2(self,aux2):
        self.aux2=aux2

    def SetAux3(self,aux3):
        self.aux3=aux3


if __name__ == "__main__":
    Quicksort()
