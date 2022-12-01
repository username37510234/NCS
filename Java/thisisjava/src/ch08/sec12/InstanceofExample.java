package ch08.sec12;

public class InstanceofExample {

	public static void main(String[] args) {
		Taxi tax = new Taxi();
		Bus bus = new Bus();
		
		ride(tax);
		System.out.println();
		ride(bus);
		
	}
	
	public static void ride(Vehicle vehicle) {
		if(vehicle instanceof Bus bus) {
			bus.checkFare();
		}
		
		vehicle.run();
	}

}
