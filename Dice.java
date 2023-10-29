/* Jennifer Sung APCSA B4
 * This program asks user to input a number and generates a pair of random
 * numbers between 1~6 (rolling the die twice).
 * Then, it will print out the frequency of each combination that were rolled.
 * (** I considered a,b and b,a the same combination **)
 */

public class Dice {
	
	// declare variable
	public int roll;
	
	// declare arrays
	public int[] d1 = new int[15];
	public int[] d2 = new int[15];

	// generate random int between 1~6
	public int Rand() {
		return(int)(Math.random()*5)+1;
	}
	
	// generate pairs of random numbers based on the user input (roll dice)
	public void RollDice(int n){
		for (int count=0; count<n; count++) {
			d1[count]=Rand();
			d2[count]=Rand();
		}
	}
	
	// find the frequency of each pairs & print the result
	public void combination(int n) {
		for (int count=0; count<n; count++) {
			// declare variables
			int fir = 0;
			int sec = 0;
			int freq = 0;
			// only happen when the combination is made with numbers between 1~6
			if (d1[count]!=0) {
				// assign values
				fir = d1[count];
				sec = d2[count]; 
				for (int x=0;x<n;x++) {
					// if (x,y) = (a,b)
					if (d1[x]==fir && d2[x]==sec) {
						// increase frequency
						freq++;
						// replace the elements in that index to 0 so it is not counted again
						d1[x]=0;
						d2[x]=0;
					// if (x,y) = (b,a) do the same thing as (a,b)
					}else if (d1[x]==sec && d2[x]==fir) {
						freq++;
						d1[x]=0;
						d2[x]=0;
					}
				// print result
				} System.out.println(fir+" and "+sec+" "+freq+" times.");
			}
			
			
		}
	}
	

	
}
