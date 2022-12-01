package ch02.sec13;

import java.util.Scanner;
public class ScannerExample {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("x값 입력: ");
		String strX = scanner.nextLine();
		int x = Integer.parseInt(strX);

		System.out.print("y값 입력: ");
		String strY = scanner.nextLine();
		int y = Integer.parseInt(strY);
		
		int result = x + y;
		System.out.printf("x + y: %d\n\n",result);
		
		while(true) {
			System.out.print("입력 문자열(종료:q): ");
			String data = scanner.nextLine();
			if(data.equals("q")) {
				break;
			}
			System.out.printf("출력 문자열: %s\n\n",data);
		}
		
		System.out.println("종료");
		scanner.close();
	}

}
