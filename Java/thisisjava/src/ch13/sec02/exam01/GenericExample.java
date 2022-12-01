package ch13.sec02.exam01;

public class GenericExample {

	public static void main(String[] args) {
		
		Product<Tv, String> p1 = new Product<>();
		
		p1.setKind(new Tv());
		p1.setModel("스마트 TV");
		
		Tv tv = p1.getKind();
		String tvM1 = p1.getModel();
		
		Product<Car, String> p2 = new Product<>();
		
		p2.setKind(new Car());
		p2.setModel("SUV자동차");
		
		Car car = p2.getKind();
		String carM1 = p2.getModel();
		
		System.out.println(p1.toString());
		System.out.println(p2.toString());
	}

}
