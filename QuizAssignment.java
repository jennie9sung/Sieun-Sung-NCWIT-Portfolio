/* Jennifer Sung APCSA Block4
 * This program contains 5 questions with each 5 answer choices.
 * If the user gets right, it will program will print a congratulatory message, and if wrong it will tell the correct answer.
 * At last, this program will print the # of correct and wrong questions and the percentage of questions he/she got right.
 */
import java.util.Scanner;
public class QuizAssignment {

	public static void main(String[] args) {
		// declare variables
		int ans=0, guess;
		int correct=0, wrong=0;
		double per=0;
		String question="";
		String choices="";
		// questions list
		String q1= "How many series in total are there in Harry Potter?";
		String q2= "How many players are in 1 soccer team?";
		String q3= "What element does 'N' represent on the periodic table?";
		String q4= "How many countreis are in the world?";
		String q5= "Which is not one of the five senses?";
		// answer choices list
		String ch1= "1)3  2)4  3)5  4)6  5)7";
		String ch2= "1)5  2)9  3)18  4)11  5)7";
		String ch3= "1)Neon  2)Nitrogen  3)Nobelium  4)Neodymium  5)Nickel";
		String ch4= "1)100  2)436  3)195  4)167  5)387";
		String ch5= "1)Emotion  2)Taste  3)Smell  4)Touch  5)Hearing";
		// user input
		Scanner reader = new Scanner(System.in);
		// as count increases by 1, move on to the next question
		for (int count=1; count<6; count++) {
			// as count increases by 1, set the question, answer, and answer choices that correlate to that number
			switch (count) {
			case 1:
				question = q1;
				ans =5;
				choices = ch1;
				break;
			case 2:
				question = q2;
				ans =4;
				choices = ch2;
				break;
			case 3:
				question = q3;
				ans =2;
				choices = ch3;
				break;
			case 4:
				question = q4;
				ans =3;
				choices = ch4;
				break;
			case 5:
				question= q5;
				ans =1;
				choices = ch5;
				break;
			}
			// print question and answer choices
			System.out.println(question);
			System.out.println(choices);
			// gets user input(guess)
			guess = reader.nextInt();
			// if user's guess gets right, print a congratulatory message and add 1 to the number of correct answers
			if (guess==ans) {
				correct++;
				System.out.println("Correct!");
			// if user's guess gets wrong, tell them the correct answer and add 1 to the number of correct answers
			}else {
				wrong++;
				System.out.println("Wrong, the answer was "+ans);
			}
		}
		// print out # of correct/wrong answers
		System.out.println("You got "+correct+" questions correct and "+wrong+" questions wrong.");
		// calculate % of correct answers and print
		per = (double)correct/5*100;
		System.out.println("You got "+(int)per+"% of the questions correct.");
		

	}

}
