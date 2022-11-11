package ch08.sec11.exam02;

public class DriverExample {

	public static void main(String[] args) {
		Driver dr = new Driver();
		
		Bus bus = new Bus();
		Taxi taxi = new Taxi();
		
		dr.drive(bus);
		dr.drive(taxi);
	}

}
