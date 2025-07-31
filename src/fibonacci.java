import java.util.Scanner;
public class fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Cuantos numeros de Fibonacci desea: ");
        int n=sc.nextInt();
        int [] fibo = new int[n];
        for (int i = 1; i < n; i++) {
            fibo[i]= fibo[i-1] + fibo[i+2];
        }
        System.out.println("Serie Fibonacci: ");
         for (int i = 1; i < n; i++) {
            System.out.println(fibo[i]);
        }
    }
}
