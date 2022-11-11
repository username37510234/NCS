package ch04.sec03;

public class SwitchCharExample {

	public static void main(String[] args) {
		char grade = 'B';
		
		switch(grade) {
		case 'A':
		case 'a':
			System.out.print("우수회원입니다.");
			break;
		case 'B':
		case 'b':
			System.out.print("일반회원입니다.");
			break;
		default:
			System.out.print("손님입니다.");
		}
	}

}
