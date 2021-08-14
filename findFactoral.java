/*
Coding challenge: calculate the factoral of a number given by the user 
*/

import java.util.Scanner;

public class findFactoral {
    public static int calcFactoral(int num){         //function to calculate the factorial of any given number
        int fact = num;
        for (int i = num-1; i > 0; i --){
            fact = fact*i;
        }
        return fact;
    }
    
    public static int recursionFactorial(int num){//calculate the factorial of a number using recursion 
        if (num == 0){
            return 1;
        }
        else{
            return (num*recursionFactorial(num-1));
        }
    }

    public static void main (String []args){
        Scanner myScanner = new Scanner(System.in); //Creating a scanner object
        System.out.println("Enter a number: ");     //Use scanner to get user input

        int userNumber = Integer.parseInt(myScanner.nextLine()); //Read the user input and cast it to an integer

        //int fact = calcFactoral(userNumber);
        int fact = recursionFactorial(userNumber);
        System.out.println("The factorial is: "+fact);
    }
}
