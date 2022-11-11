package ch13.sec02.exam01;

public class GenericExample {

	public static void main(String[] args) {
		Product<Tv, String> pro1 = new Product<>();
		
		pro1.setKind(new Tv());
		pro1.setModel("스마트Tv");
		
		Tv tv = pro1.getKind();
		String tvModel = pro1.getModel();
		
		System.out.println(tv);
		System.out.println(tvModel);
		
		Product<Car, String> pro2 = new Product<>();
		
		pro2.setKind(new Car());
		pro2.setModel("SUV자동차");
		
		Car car = pro2.getKind();
		String carModel = pro2.getModel();
		
		System.out.println(car);
		System.out.println(carModel);
	}

}
