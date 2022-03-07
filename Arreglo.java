import java.util.*;

public class Arreglo {
    //Arraylist<int> arrayAux = new Arraylist<int>();
    static ArrayList<Integer> Aux = new ArrayList<Integer>();
    public static void main(String[] args) {
        
        int pos = 0;
        int n = 0;
        int suma = 0;
        int aux[] = new int[10];

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        int a[] = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Aux.add(2);
        /*
         * for(int i=0; i<n;i++){ int j=i+1; while(j<n-1){ suma = sum(a,i,j); if (suma
         * ==0){ System.out.println("entra porque sum es 0 "+" j e i "+(j-i)); aux[pos]
         * = (j-i); pos++; break; }else{ j++; } } }
         * 
         * for(int i=0;i<aux.length;i++){ System.out.println(aux[i]); }
         */

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {

                suma = sum(a, i, j);

                if (suma == 0) {
                    aux[pos] = j - i;
                    pos++;
                    break;
                }
            }
        }
        MetodoInsertSort(aux);
        System.out.println(aux[0]);
    }

    public static void MetodoInsertSort(int array[]) {
        int pibote;
        for (int i = 1; i < (array.length); i++) {
            int j = i;
            while (j > 0 && array[j - 1] > array[j]) {
                pibote = array[j - 1];
                array[j - 1] = array[j];
                array[j] = pibote;
                j--;
            }
        }
    }

    public static int sum(int a[], int i, int j) {

        int suma = 0;

        for (int x = i; x <= j; x++) {

            suma = suma + a[x];

        }

        return suma;
    }
    /*
     * public static void main(String[] args) { Subsecuencia sub = new Subsecuencia
     * ();
     * 
     * 
     * 
     * } /*int arregloNum[]; Scanner scanNum = new Scanner(System.in);
     * 
     * System.out.println("De que tamaño es el arreglo?"); int tamArray =
     * scanNum.nextInt(); arregloNum=new int [tamArray];
     * 
     * System.out.println("Digite los numeros del arreglo");
     * 
     * for(int i=0 ; i<tamArray ; i++){
     * 
     * }
     */

}