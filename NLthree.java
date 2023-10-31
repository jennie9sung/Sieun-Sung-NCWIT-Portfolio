/* Jennifer Sung APCSA B4
 * This program creates a multiplication table based on the user's number input
 */
import java.util.Scanner;

public class NLthree {

	public static void main(String[] args) {
		// declare var
		int max=0;
		// get user input
		Scanner reader = new Scanner(System.in);
		System.out.println("Type a number: ");
		max = reader.nextInt();
		// print the first row of numbers
		for(int count1=0; count1<=max; count1++) {
			if (count1==0) {
				System.out.print(" "+"\t");
			}else {
			System.out.print(count1+"\t");
			}
		}
		System.out.println("");
		// print a line that divides the number rows and the multiplication rows
		for(int count1=0; count1<=max; count1++) {
			System.out.print("_"+"\t");
			}
		System.out.println("");
		for(int mult=1; mult<=max; mult++) {
			// print a line that divides the number columns and the multiplication columns + print the first column
			System.out.print(mult+"|"+"\t");
			for (int first=1; first<=max; first++) {
				// print the multiplications
					System.out.print(mult*first+"\t");
				}System.out.println("");
			
			}
		}
	}




