package ch04.sec03;

public class SwitchExample {

	public static void main(String[] args) {
		int num = (int)(Math.random()*6)+1;
		
		switch(num) {
		case 1:
			System.out.print("1번이 나왔습니다.");
			break;
		case 2:
			System.out.print("2번이 나왔습니다.");
			break;
		case 3:
			System.out.print("3번이 나왔습니다.");
			break;
		case 4:
			System.out.print("4번이 나왔습니다.");
			break;
		case 5:
			System.out.print("5번이 나왔습니다.");
			break;
		default:
			System.out.print("6번이 나왔습니다.");
		}
	}

}
