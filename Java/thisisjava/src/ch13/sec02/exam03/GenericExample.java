package ch13.sec02.exam03;

public class GenericExample {

	public static void main(String[] args) {
		Box b1 = new Box();
		b1.content = "100";
		
		Box b2 = new Box();
		b2.content = "100";
		
		Box b3 = new Box();
		b3.content = 100;
		
		boolean result1 = b1.compare(b2);
		System.out.println("result1: " + result1);
		
		boolean result2 = b1.compare(b3);
		System.out.println("result2: " + result2);
	}

}
