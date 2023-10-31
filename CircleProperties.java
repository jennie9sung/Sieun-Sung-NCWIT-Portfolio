// Jennifer Sung

/* This program asks the user to input the radius of the
 * sphere and then calculates the diameter, circumference, 
 * surface area, and the volume of the sphere based on that radius.
 */


import java.util.Scanner;

public class CircleProperties {
	public static void main(String[] args) {
		Scanner radius = new Scanner(System.in);
		// declare variables
		double rad, dia, cir, sur, vol;
		
		// read in the radius of the sphere
		System.out.println("What is the radius of the sphere?");
		rad = radius.nextDouble();
		
		/* calculate diameter, circumference, surface area, and
		 * the volume of the sphere based on the user input.
		 */
		dia = rad*2;
		cir = rad*2*3.14;
		sur = rad*rad*4*3.14;
		vol = rad*rad*rad*4/3*3.14;
		
		// print out the calculation result
		System.out.println("Diameter = "+ dia);
		System.out.println("Circumference = "+ cir);
		System.out.println("Surface Area = "+ sur);
		System.out.println("Volume = "+ vol);
		

	}

}
