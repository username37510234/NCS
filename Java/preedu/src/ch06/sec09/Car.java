package ch06.sec09;

public class Car {

	String model;
	int speed;
	
	Car(String model){
		this.model = model;
	}
	
	void setSpeed(int speed) {
		this.speed = speed;
	}
	
	void run() {
		this.setSpeed(100);
		System.out.printf("%s가 달립니다.\t(시속:%03dkm/h)\n",model,speed);
	}
}
