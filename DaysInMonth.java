/* Jennifer Sung, APCSA Block 4
 * This program asks the user to input the month and the year
 * and based on those input, this program will calculate and print
 * out how many days are in 
 */
import java.util.Scanner;
public class DaysInMonth {

	public static void main(String[] args) {
		// declare variables
		String m;
		int y, d=0;
		// ask for user input(month, year)
		Scanner month = new Scanner(System.in);
		System.out.println("Type a month in upper cases: ");
		m = month.next();
		Scanner year = new Scanner(System.in);
		System.out.println("Type a year: ");
		y = year.nextInt();
		// classify/calculate the number of days
		switch (m) {
		case "JANUARY":
			d=31;
			break;
		case "FEBRUARY":
			if (y%4==0) {
				d=29;
			}else {
				d=28;
			}
			break;
		case "MARCH":
			d=31;
			break;
		case "APRIL":
			d=30;
			break;
		case "MAY":
			d=31;
			break;
		case "JUNE":
			d=30;
			break;
		case "JULY":
			d=31;
			break;
		case "AUGUST":
			d=31;
			break;
		case "SEPTEMBER":
			d=30;
			break;
		case "OCTOBER":
			d=31;
			break;
		case "NOVEMBER":
			d=30;
			break;
		case "DECEMBER":
			d=31;
			break;
		}
		// print the result
		System.out.println("There are "+d+" days in "+m+", "+y+".");

	}
}