/* Jennifer Sung APCSA B4
 * 
 * This program is called 'Minesweeper.' It will print out a gameboard with instructions first.
 * The user will try to guess the row and the column that doesn't have a bomb placed on it.
 * If the user chooses spaces with bombs for 3 times, the game ends and the program will print a message.
 * If the user guesses all the non-bomb spaces, the game ends and the program will print out a 'congratulation message.'
 * Every time a user chooses a space, the program will let know if that was a bomb or not and print an updated gameboard.
 */

import java.util.Scanner;

public class TwoDArray {
	// declare a private 2D array
	private static String [][] gameboard = new String[5][5];

	public static void main(String[] args) {
		Scanner reader = new Scanner(System.in);
		// declare variables + array
		int end=0;
		int row=0;
		int column=0;
		int left=15;
		int lives=3;
		int print=0;
		
		String [][] gamemap = new String[5][5];
		
		// assign blank spaces
		for (int count=0; count<5; count++) {
			for(int num=0;num<5;num++) {
				gameboard[count][num]="□";
				gamemap[count][num]="□";
			}
		}
		
		// generate bombs in random coordinates
		for (int num=0;num<10;num++) {
			int rand1=randnum();
			int rand2=randnum();
			if (gamemap[rand1][rand2]=="B") {
				num-=1;
			}else {
				gamemap[rand1][rand2]="B";
			}

		}
		
		// this part is just to check if the program is operating properly
		
//		System.out.println("----------------ANSWER----------------");
//		System.out.println("");
//		for(int x=0; x<6;x++) {
//			System.out.print(x+"\t");
//		}
//		System.out.println("");
//		System.out.println("");
//		for (int count=0; count<5; count++) {
//			System.out.print(count+1+"\t");
//			for(int num=0;num<5;num++) {
//				System.out.print(gamemap[count][num]+"\t");				
//			}
//			System.out.println("");
//			System.out.println("");
//		}
		
		// print instructions
		System.out.println("Welcome to Minesweeper!");
		System.out.println("Try to guess all the non-bomb spaces.");
		System.out.println("'B' represents bomb spaces and 'O' represents non-bomb spaces.");
		System.out.println("There are 10 bombs and you have 3 lives.");
		System.out.println("");
		System.out.println("");
		
		// do loop that loops back until the game ends
		do {
			// print previous round's result
			if (print==1) {
				System.out.println("You chose a bomb! You got "+lives+" lives left.");
				print=0;
			}else if(print==2) {
				System.out.println("You chose correctly!");
			}
			
			// print game board to show the updated game visual		
			System.out.println("----------------MINESWEEPER----------------");
			System.out.println("");
			printtrack();
			
			// get user input
			System.out.println("Choose a row: ");
			row = reader.nextInt()-1;
			System.out.println("Choose a column: ");
			column = reader.nextInt()-1;
			
			//check if user chose a bomb
			if (gamemap[row][column]=="B") {
				gameboard[row][column]="B";
				lives-=1;
				print=1;
			}else {
				gameboard[row][column]="O";
				left-=1;
				print=2;
//				System.out.println(left);
			}
			
			// final result if game ends
			if (lives==0) {
				System.out.println("");
				System.out.println("You lost this game!");
				printtrack();
				end=1;
			}else if(left==0) {
				System.out.println("");
				System.out.println("Congratulations! You won this game!");
				printtrack();
				end=1;
			}

			
		}while(end!=1);

	}

	// method to generate random integers
	public static int randnum() {
		int n=(int)(Math.random()*5);
		return n;
	}
	
	// printout gameboard(provide visual to the user)
	public static void printtrack() {
		for(int x=0; x<6;x++) {
			System.out.print(x+"\t");
		}
		System.out.println("");
		System.out.println("");
		for (int count=0; count<5; count++) {
			System.out.print(count+1+"\t");
			for(int num=0;num<5;num++) {
				System.out.print(gameboard[count][num]+"\t");				
			}
			System.out.println("");
			System.out.println("");
		}
	}

}
	



