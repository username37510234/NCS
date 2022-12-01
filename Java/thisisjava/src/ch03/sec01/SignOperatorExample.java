package ch03.sec01;

public class SignOperatorExample {

	public static void main(String[] args) {
		int x = -100;
		x = -x;
		System.out.printf("x: %d\n",x);
		
		byte b = 100;
		byte y = (byte)-b;
		System.out.printf("y: %d", y);
	}

}
