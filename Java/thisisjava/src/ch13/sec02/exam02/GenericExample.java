package ch13.sec02.exam02;

public class GenericExample {

	public static void main(String[] args) {
		HomeAgency hA = new HomeAgency();
		Home Ho = hA.rent();
		Ho.turnOnLight();
		
		CarAgency cA = new CarAgency();
		Car ca = cA.rent();
		ca.run();
	}

}
