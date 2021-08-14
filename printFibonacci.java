/*
Coding challenge: print out the fibonacci sequence 
*/

import java.util.ArrayList;

class printFibbonacci{
    static ArrayList<Integer> fibbonacci(int range){
        ArrayList<Integer> fib = new ArrayList<Integer>();
        fib.add(1);
        fib.add(1);
        for (int i = 2; i < range; i ++){
            fib.add(fib.get(i-1) + fib.get(i - 2));
        }
        return fib;
    }

    public static void main (String []args){
        System.out.println(fibbonacci(10));
    }
}