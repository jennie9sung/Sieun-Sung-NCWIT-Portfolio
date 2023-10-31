// Jennifer Sung Block 4
/* This program asks users to input their score for a test. 
 * Then, it will decide the grade they will get for that test based on their score.
 * Finally it will print out the result.
 */

import java.util.Scanner;
public class Grade {
	public static void main(String[] args) {
		// declare variables
		int score;
		char grade;
		// read in user's score
		Scanner test = new Scanner(System.in);
		System.out.println("Enter your score for a test: ");
		score = test.nextInt();
		// calculate/decide the grade based on the score input
		if (score>=90){
			grade = 'A';
		} else if (score>=80) {
			grade = 'B';
		} else if (score>=70) {
			grade = 'C';
		} else if (score>=60) {
			grade = 'D';
		} else {
			grade = 'F';
		}
		// print out the result
		System.out.println("Your grade for that test is "+grade+".");
	}

}
