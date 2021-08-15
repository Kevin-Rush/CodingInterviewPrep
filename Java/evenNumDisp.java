package Java;
/*
Coding challenge: print out a list of even numbers
*/

import java.util.ArrayList;

public class evenNumDisp {
    public static void main (String []args){
        ArrayList<Integer> array = new ArrayList<Integer>();
        for(int i = 0; i < 10; i ++){
            array.add(i*2);
        }
        System.out.println(array);
    }
}
