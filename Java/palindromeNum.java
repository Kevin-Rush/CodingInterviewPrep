package Java;
/*
Coding challenge: determine if a number is a palindrome or not
*/
public class palindromeNum {
    static boolean isPalind(Long num){
        String strNum = Long.toString(num);//Long is used instead of Integer to allow for bigger numbers
        boolean check = true;
        int strLen = strNum.length();
        for(int i = 0; i < strLen/2; i ++){
            //System.out.println(strNum.charAt(i) + " & " + strNum.charAt((strLen-1) - i));
            if (strNum.charAt(i) != strNum.charAt((strLen-1) - i)){ //compare the first with the last and then keep working inwards towards the middle
                check = false;
            }
        }

        return check;
    }

    static boolean isPalindromeSTRB(Long num){
        if(num == null)
            return false;
        String strNum = Long.toString(num);
        StringBuilder strBuild = new StringBuilder(strNum);
        strBuild.reverse();
        return strBuild.toString().equals(strNum);
    }

    public static void main(String []args){
        System.out.println(isPalindromeSTRB(123456789987654321L));
    }
}
