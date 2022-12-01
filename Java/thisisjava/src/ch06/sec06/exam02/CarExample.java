package ch06.sec06.exam02;

public class CarExample {

	public static void main(String[] args) {

		Car myC = new Car();

		System.out.println("제작회사: "+myC.company);
		System.out.println("모델명: "+myC.model);
		System.out.println("색깔: "+myC.color);
		System.out.println("최고속도: "+myC.maxSpeed);
		System.out.println("현재속도: "+myC.speed);
		
		myC.speed = 60;
		System.out.println("수정된 속도: "+myC.speed);
	}

}
