/* Jennifer Sung APCSA B4
 * This program asks the user to input a value and display the converted value.
 * They will have a total of 6 options of units they want to convert.
 * At the last, the program will print out the converted value with the units.
 */

// Scanner
import java.util.Scanner;
public class methodQ1 {
    public static void main(String[] args){
    	// declare variables
        String unit="";
        double result=0;
        Scanner reader = new Scanner(System.in);
        // print conversion unit options 
        print("Choose the conversion you want: ");
        print("1: ft->in");
        print("2: cm->in");
        print("3: mi->m");
        print("4: mi->ft");
        print("5: lb->oz");
        print("6: kW->hp");
        // conversion unit type
        int type= reader.nextInt();
        // ask for a number
        print("Type a number you want to convert:");
        double value = reader.nextDouble();
        // based on the conversion unit type input, call the appropriate method
        switch(type) {
            case(1):
                result = ftin(value);
                unit = "in";
                break;
            case(2):
            	result=cmin(value);
            	unit ="in";
            	break;
            case(3):
            	result=mim(value);
            	unit ="m";
            	break;
            case(4):
            	result=mift(value);
            	unit ="ft";
            	break;
            case(5):
            	result=lboz(value);
            	unit ="oz";
            	break;
            case(6):
            	result=kWhp(value);
            	unit ="hp";
            	break;    
        }
        // print result
        print(result+unit);
}
    
    // println method
    public static void print(String statement) {
        System.out.println(statement);
        }
    // convert ft->in    
    public static double ftin(double num) {
        return(num*12);
        }
    // convert cm->in
    public static double cmin(double num) {
        return(num/2.54);
        }
    // convert mi->m
    public static double mim(double num) {
        return(num*1609);
        }
    // convert mi->ft
    public static double mift(double num) {
        return(num*5280);
        }
    // convert lb->oz
    public static double lboz(double num) {
        return(num*16);
        }
    // convert kW->hp
    public static double kWhp(double num) {
        return(num*1.341003);
        }

}