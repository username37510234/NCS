package ch02.sec13;

import java.util.Scanner;
public class ScannerExample {
	public static void main(String[] args) throws Exception{
		Scanner scan1 = new Scanner(System.in);
		
		System.out.print("x 값 입력: ");
		String strX = scan1.nextLine();
		int x = Integer.parseInt(strX);
		
		System.out.print("y 값 입력: ");
		String strY = scan1.nextLine();
		int y = Integer.parseInt(strY);
		
		int result = x + y;
		System.out.println("x+y: "+result);
		System.out.println();
		
		while(true) {
			System.out.print("입력 문자열('q'를 입력하면 종료됩니다): ");
			String data = scan1.nextLine();
			if(data.equals("q")) {
				break;
			}
			System.out.println("출력 문자열: "+data);
			System.out.println();
		}
		System.out.print("종료");
	}
}
