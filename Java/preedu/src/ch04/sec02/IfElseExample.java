package ch04.sec02;

import java.util.Scanner;
public class IfElseExample {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.print("점수를 입력하세요.");
		String inputdata = scanner.nextLine();
		int score = Integer.parseInt(inputdata);
		
		if(score>=90) {
			System.out.println("점수가 90보다 큽니다.");
			System.out.print("등급은 A입니다.");
		} else if (score>=80){
			System.out.println("점수가 80보다 큽니다.");
			System.out.print("등급은 B입니다.");
		} else if (score>=70){
			System.out.println("점수가 70보다 큽니다.");
			System.out.print("등급은 C입니다.");
		} else {
			System.out.println("점수가 70보다 작습니다.");
			System.out.print("등급은 D입니다.");
		}
		scanner.close();
	}

}
