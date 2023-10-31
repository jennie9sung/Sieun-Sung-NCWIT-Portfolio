/* Jennifer Sung APCSA Block 4
 * This program asks a user to input a random integer between 1~20.
 * Then, the program tries to guess the number that the user assigned.
 * When the computer guesses the number correctly, it prints out a message
 * and the number of guesses that the computer made.
 */
import java.util.Scanner;
import java.util.Random;
public class ComputerGuess {
	public static void main(String[] args) {
		Scanner reader = new Scanner (System.in);
		Random rand = new Random();
		// declare variables
		int min=1, max=20, ans=0, guess=0, times=0;
		// ask a user to assign a random number between 1~20
		System.out.println("Type in a random number between 1~20");
		ans = reader.nextInt();
		// computer generates a random guess
		guess = (int)Math.floor(Math.random()*(max-min+1)+min);
		do {
			System.out.println(guess);
			// count number of times the computer tries to guess until it gets it right
			times ++;
			// classify if the number is too high or low
			if (guess>ans) {
				System.out.println("Too high!");
				max = guess;
				// limit the random guesses
				guess = (int)Math.floor(Math.random()*(max-min+1)+min);
			} else if (guess<ans){
				System.out.println("Too low!");
				min = guess;
				// limit the random guesses
				guess = (int)Math.floor(Math.random()*(max-min+1)+min);
			}
		// classify the guess if the guess was wrong
		} while (guess!=ans);
		// print final guess
		System.out.println(guess);
		times ++;
		// print a message and the number of times since the computer got the answer right
		System.out.println("The computer correctly guessed your number.");
		System.out.println("It took "+times+" times for the computer to guess your number.");


	}

}
