package Java;

public class removeElementInString {
    static String remAllElements(String str, String element){
        if (str == null)
            return null;
        return str.replace(element, "");
    }
    static String remFirstElement(String str, String element){
        if (str == null)
            return null;
        StringBuilder temp = new StringBuilder(str);
        int index = temp.indexOf(element);
        temp.deleteCharAt(index);
        return temp.toString();
    }
    public static void main (String []args){
        String str = "hello world";
        String element = "l";
        System.out.println("Delete ALL '"+element+"' from "+str+": " + remAllElements(str, element));
        System.out.println("Delete FIRST '"+element+"' from "+str+": " + remFirstElement(str, element));
    }
}
