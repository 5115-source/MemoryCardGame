package lab2;
import java.util.ArrayList;

public class Program2 {
  public static void main(String[] args) {
    // Generate a lottery
    int randomNumber = (int)(Math.random()*1000);
    String lottery = String.format("%03d", randomNumber);
    ArrayList<Integer> lotteryNumList = new ArrayList<Integer>();
    for (int i = 0 ; i < lottery.length(); i++){
      lotteryNumList.add(Character.getNumericValue(lottery.charAt(i)));   
     }
    
    // Prompt the user to enter a guess
    java.util.Scanner input = new java.util.Scanner(System.in);
    System.out.print("Enter your lottery pick (three digits): ");
    String guess = input.nextLine();
    ArrayList<Integer> guessNumList = new ArrayList<Integer>();
    for (int i = 0 ; i < guess.length(); i++){
      guessNumList.add(Character.getNumericValue(guess.charAt(i)));   
     }
     //checking matchCount
     int matchCount =0;
     for(int digit : guessNumList ){
      if(lotteryNumList.contains(digit)){
        matchCount++;
      }
     }

     System.out.println(lottery);
    
     //checking
     if(guess == lottery){
      System.out.println("Exact match: you win $10,000");
      return;
     }
     switch (matchCount) {
      case 3:
      System.out.println("Match all digits: you win $3,000");
      break;
      case 2:
      System.out.println("Match 2 digits: you win $2,000");
      break;
      case 1:
      System.out.println("Match 1 digits: you win $1,000");
      break;
      default:
      System.out.println("Sorry, no match");        
      break;
     }

     }

  }
