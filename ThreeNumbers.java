// Jennifer Sung Block 4
/* this program asks the user to enter 3 integers. Then, it will find the largest
 * and the smallest number and the average and print the result.
 */
 
import java.util.Scanner;

public class ThreeNumbers {

	public static void main(String[] args) {
		// declare variables
		int n1, n2, n3, largest = 0, smallest = 0;
		double average;
		// read in the three numbers
		Scanner first = new Scanner(System.in);
		System.out.println("Type in the first integer:");
		n1 = first.nextInt();
		Scanner second = new Scanner(System.in);
		System.out.println("Type in the second integer:");
		n2 = second.nextInt();
		Scanner third = new Scanner(System.in);
		System.out.println("Type in the third integer:");
		n3 = third.nextInt();
		
		// classify the numbers (find the largest, smallest number and save it to a variable)
		if (n1>=n2 && n1>=n3) {
			largest = n1;
			if (n2>=n3) {
				smallest = n3;	
			} else {
				smallest = n2;
			}
		}else {
			smallest = n1;
			if (n2>=n3) {
				largest = n2;
				if (n1>=n3) {
					smallest = n3;
				}
			} else {
				largest = n3;
				if (n1>=n2) {
					smallest = n2;
				}
			}
		}
		
		// calculate the average of the three numbers
		average = ((double)n1+n2+n3)/3;
		
		// print out the results
		System.out.println("Largest number: "+largest);
		System.out.println("Smallest number: "+smallest);
		System.out.println("Average: "+average);
	}

}