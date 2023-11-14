/* Jennifer Sung Block 4
 * This program asks a user to input his/her maximum monthly values
 * for talk minutes used, text messages sent, and gigabytes of data used.
 * Then, the program recommends and prints a plan(program) based on those inputs.
 */
import java.util.Scanner;
public class HorizonPhones {

	public static void main(String[] args) {
		// declare variables
		int talk, text, data, price;
		char program;
		// asks user input about their maximum monthly values
		Scanner q1 = new Scanner(System.in);
		System.out.println("What is your maximum monthly values for talk minutes used?");
		talk = q1.nextInt();
		Scanner q2 = new Scanner(System.in);
		System.out.println("What is your maximum monthly values for text messages sent?");
		text = q2.nextInt();
		Scanner q3 = new Scanner(System.in);
		System.out.println("What is your maximum monthly values for gigabytes of data used?");
		data = q3.nextInt();
		// find the plan(program) and the price of it that fits the user input
		if (data==0) {
			if (talk<500) {
				if (text==0) {
					program = 'A';
					price = 49;
				} else {
					program = 'B';
					price = 55;
				}
			} else if (text<100) {
				program = 'C';
				price = 61;
			} else {
				program = 'D';
				price = 70;
			}
		} else if (data<3) {
			program = 'E';
			price = 79;
		} else {
			program = 'F';
			price = 87;
		}
		
		// prints out the result
		System.out.println("Your recommended plan from Horizon Phones is plan "+program+".");
		System.out.println("You can accept plan "+program+" at $"+price+" per month.");
		

	}

}
