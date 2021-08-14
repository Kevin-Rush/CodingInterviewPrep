import java.util.Scanner;

public class findFactoral {
    public static int calcFactoral(int num){         //function to calculate the factorial of any given number
        int fact = num;
        for (int i = num-1; i > 0; i --){
            fact = fact*i;
            System.out.println(fact);
        }
        return fact;
    }

    public static void main (String []args){
        Scanner myScanner = new Scanner(System.in); //Creating a scanner object
        System.out.println("Enter a number: ");     //Use scanner to get user input

        int userNumber = Integer.parseInt(myScanner.nextLine()); //Read the user input and cast it to an integer

        int fact = calcFactoral(userNumber);
        System.out.println("The factorial is: "+fact);
    }
}
