package ch03.sec11;
import java.util.Scanner;
public class Conditional10perationExample {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("점수를 입력하세요.");
		String inputdata = scanner.nextLine();
		int score = Integer.parseInt(inputdata);
		char grade = (score>90) ? 'A' : ((score>80) ? 'B' : 'C' );
		System.out.print(score+"점은 "+grade+"등급입니다.");
		scanner.close();
	}

}
