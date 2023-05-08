
// javac Main.java
// java Main

public class Main {

    public static void main(String [] argv){
        System.out.println("Laboratorio 1");
        int result = sum(2,2);
        int resultWithMe = dependWithMe(2,2);
        System.out.println("La suma es "+ result);
        System.out.println("La operacion es "+ resultWithMe);
    }

    public static  int sum(int x, int y){
        return  x+y;
    }
    public static int dependWithMe(int x, int y) {
        if (x > y) {
            return x * y;
        }
        if (x < y) {
            return (x * y) - (x + y);
        }
        return (x * y) * 2;
    }
}