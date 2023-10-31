// Jennifer Sung

/* This program asks the user to input the number of eggs
 * in the order and then displays the total cost with explanation of it.
 */
import java.util.Scanner;
public class Eggs {

	public static void main(String[] args) {
		Scanner eggs = new Scanner(System.in);
		
		// declare variables
		int totalE, dEgg, iEgg; // total eggs, dozen eggs, individual eggs
		double price; // total price
		
		// read in number of eggs in the order
		System.out.println("How many eggs did you order?");
		totalE = eggs.nextInt();
		
		// calculate the number of dozen eggs and individual eggs
		dEgg = totalE/12;
		iEgg = totalE-dEgg*12;
		// calculate total price
		price = dEgg*3.25+iEgg*0.45;
		// print out total price and explanation
		System.out.println("You ordered "+totalE +" eggs.");
		System.out.println("That's "+dEgg+" dozen at $3.25 per dozen and "+iEgg+" loose eggs at 45 cents each for a total of $"+price+".");


	}

}
