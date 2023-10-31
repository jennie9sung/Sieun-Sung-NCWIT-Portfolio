// Jennifer Sung B4
/* This program asks the user to input 2 numbers and then solve for and print out
 * the sum of all integers between those two numbers.
 */

import java.util.Scanner;
public class CalcSum {

	public static void main(String[] args) {
		// declare variables
		int first=0, second=0, sum=0, count, add;
		// ask user to input 2 numbers
		Scanner reader = new Scanner (System.in);
		System.out.println("Enter a number: ");
		first = reader.nextInt();
		System.out.println("Enter a different number: ");
		second = reader.nextInt();
		// calculate the sum of all numbers
		// declare the smallest and largest numbers as min and max of the range
		
		if (first<second) {
			for (count=first; count<=second; count++)
				sum = sum+count;
		} else {
			for (count=second; count<=first; count++)
				sum = sum+count;
		}
		// print out the result
		System.out.println("The sum of all integers between "+first+" and "+second+" is "+sum+".");

	}

}
