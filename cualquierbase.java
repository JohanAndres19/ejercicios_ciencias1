import java.util.Scanner;
import java.util.Arrays;
class Main {
    public static void main(String[] args) {
        Conversor(1000, 16);
    }

    public static void Conversor(int numero, int base) {
        String Numero = " ";
        String invertida="";
        System.out.println("tamaño");
        char letras[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
        while (numero >= 1) {
            int residuo = numero % base;
            numero = Integer.valueOf(numero / base);
            Numero += Character.toString(letras[residuo]);
        }
        for (int indice = Numero.length() - 1; indice >= 0; indice--) {
			// Y vamos concatenando cada carácter a la nueva cadena
			invertida += Numero.charAt(indice);
		}
        System.out.println(invertida);
    }
}