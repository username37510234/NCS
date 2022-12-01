package ch08.sec10.exam02;

public class CastingExample {

	public static void main(String[] args) {
		Vehicle vh = new Bus();
		
		vh.run();
		
		Bus bus = (Bus) vh;
		bus.run();
		bus.checkFare();
	}

}
