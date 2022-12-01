package ch06.sec06.exam01;

public class CarExample {

	public static void main(String[] args) {

		Car myC = new Car();

		System.out.println("모델명: "+myC.model);
		System.out.println("시동여부: "+myC.start);
		System.out.println("현재속도: "+myC.speed);
	}

}
