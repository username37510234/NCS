package ch12.sec10;

import java.util.regex.Pattern;

public class PatternExample {

	public static void main(String[] args) {
		String regE = "(02|010)-\\d{3,4}-\\d{4}";
		String data = "010-123-4567";
		boolean result = Pattern.matches(regE, data);
		if(result) {
			System.out.println("정규식과 일치합니다.");
		} else {
			System.out.println("정규식과 일치하지 않습니다.");
		}
		
		regE = "\\w+@\\w\\.\\w+(\\.\\w+)?";
		data = "angel@mycompany.com";
		result = Pattern.matches(regE, data);
		if(result) {
			System.out.println("정규식과 일치합니다.");
		} else {
			System.out.println("정규식과 일치하지 않습니다.");
		}
	}
}
