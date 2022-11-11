package ch05.sec05;

public class CharAtExample {

	public static void main(String[] args) {
		String ssn = "9506241230123";
		char sex1 = ssn.charAt(6);
		String sex2 = switch(sex1){
		case '1','3' -> "남자";
		case '2','4' -> "여자";
		default -> "잘못된 입력";
		};
		System.out.print(sex2+"입니다.");
	}

}
