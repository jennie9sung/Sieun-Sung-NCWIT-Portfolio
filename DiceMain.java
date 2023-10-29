/* Jennifer Sung APCSA B4
 * This program asks user to input a number and generates a pair of random
 * numbers between 1~6 (rolling the die twice).
 * Then, it will print out the frequency of each combination that were rolled.
 * (** I considered a,b and b,a the same combination **)
 */

import java.util.Scanner;
public class DiceMain {

	public static void main (String[] args) {
		// Call class
		Scanner reader = new Scanner(System.in);
		Dice di = new Dice();
		
		// get user input of # of times to roll the dice
		System.out.println("How many times do you want to roll the dice? (max 15) : ");
		di.roll = reader.nextInt();
		
		// roll 2 dice
		di.RollDice(di.roll);
		
		// find frequency of combinations & print result
		di.combination(di.roll);
		
	}
	
	
	
}
