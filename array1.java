/* Jennifer Sung APCSA B4
 * This program asks the user to input 10 speeds and save those in an array.
 * Then, this program calculates and prints out the highest/lowest speed, average speed,
 * number of ppl over 0-10 miles over, number between 10-20 over, and the number over 20.
 */

import java.util.Scanner;
public class array1 {

	public static void main(String[] args) {
		// Scanner
		Scanner reader = new Scanner(System.in);
		// declare arrays
		int[] speed = new int[10];
		// declare variables
		int total=0;
		double average=0;
		int zete=0;
		int tetw=0;
		int tw=0;
		
		//		all calculations
		// get speed input
		for (int x=0;x<10;x++) {
			System.out.println("Speed: ");
			speed[x]=reader.nextInt();
		}
		// add all the speeds
		for (int x=0;x<10;x++) {
			total = total+speed[x];
		}
		// calculate the average
		average = (double)total/10;
		
		int max = speed[0];
		int min = speed[0];
		// find highest/lowest
		for (int x=1;x<10;x++) {
			if (max<speed[x]) {
				max = speed[x];
			}
			if (min>speed[x]) {
				min = speed[x];
			}
		}
		// find how many speeds exceeded 55 miles within certain intervals
		for (int x=1;x<10;x++) {
			if (speed[x]>55) {
				int n=speed[x]-55;
				if (n<=10) {
					zete++;
				}else if (n>10&&n<=20) {
					tetw++;
				}else {
					tw++;
				}
			}
		}
		// printout results
		System.out.println("Average: "+average);
		System.out.println("Highest: "+max);
		System.out.println("Lowest: "+min);
		System.out.println("0~10 miles over: "+zete);
		System.out.println("10~20 miles over: "+tetw);
		System.out.println("20~ miles over: "+tw);
		

	}

}
