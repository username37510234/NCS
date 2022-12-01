package ch08.sec05;

public class RemoteControlExample {

	public static void main(String[] args) {

		RemoteControl rc = new Television();
		rc.turnOn();
		rc.turnOff();
		rc.setVolume(5);
		
		rc.setMute(true);
		rc.setMute(false);
		
		System.out.println();
		rc = new Audio();
		rc.turnOn();
		rc.setVolume(7);
		
		rc.setMute(true);
		rc.setMute(false);
		
		rc.turnOff();
	}

}
