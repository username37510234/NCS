package ch08.sec11.exam01;

public class CarExample {

	public static void main(String[] args) {
		Car myC = new Car();
		
		myC.run();
		
		myC.tire1 = new KumhoTire();
		myC.tire2 = new KumhoTire();
		
		myC.run();
	}

}
