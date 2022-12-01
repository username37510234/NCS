package ch08.sec11.exam02;

public class DriverExample {

	public static void main(String[] args) {
		Driver drver = new Driver();
		
		Bus bus = new Bus();
		Taxi tax = new Taxi();
		
		drver.drvie(bus);
		drver.drvie(tax);
	}

}
