package ch08.sec08;

public class MultiInterfaceImplExample {

	public static void main(String[] args) {
		RemoteControl rc = new SmartTelevision();
		
		rc.turnOn();
		rc.turnOff();
		
		Searchable sc = new SmartTelevision();
		
		sc.search("http://www.youtube.com");
	}

}
