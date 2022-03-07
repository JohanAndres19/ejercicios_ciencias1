import java.util.*;
public class ejerciciofeynman {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int resultado;
        int N;
        do{
          N = entrada.nextInt(); 
          if(N!=0){ 
          resultado= (int) ((2*Math.pow(N,3)+3*Math.pow(N,2)+N)/6);
          }
         // System.out.print(resultado);
        }while(N>0);
        System.out.println("------");
    }

}
