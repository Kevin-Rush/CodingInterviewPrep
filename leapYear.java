/*
Coding challenge: determine if a year (given by the user) is a leap year
*/

import java.util.Scanner;

public class leapYear {
    static boolean isLeapYear(int year){
        boolean tof = false;
        if (year%4 == 0){
            if (year%100 == 0){
                if (year%400 == 0){
                    tof = true;
                }
                else{
                    tof = false;
                }
            }
            else{
                tof = true;
            }
        }
        return tof;
    }
    public static void main (String []args){
        Scanner myScanner = new Scanner(System.in); //Creating a scanner object
        System.out.println("Enter a number: ");     //Use scanner to get user input

        int userYear = Integer.parseInt(myScanner.nextLine()); //Read the user input and cast it to an integer

        //int fact = calcFactoral(userNumber);
        boolean year = isLeapYear(userYear);
        System.out.println("Is the year "+userYear+" a leap year? "+year);
    }
}
