package ch05.sec05;

public class CharAtExample {

	public static void main(String[] args) {
		String ssn = "9506244230123";
		
		char sex = ssn.charAt(6);
		switch (sex){
			case '1':
			case '3':
				System.out.print("남자입니다.");
				break;
			case '2':
			case '4':
				System.out.print("여자입니다.");
				break;
			default:
				System.out.print("틀렸습니다.");
		}
	}

}
