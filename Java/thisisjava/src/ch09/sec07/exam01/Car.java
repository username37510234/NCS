package ch09.sec07.exam01;

public class Car {

	private Tire tire1 = new Tire();

	private Tire tire2 = new Tire() {
		@Override
		public void roll() {
			System.out.println("익명 자식 Tire 객체 1이 굴러갑니다.");
		};
	};

	public void run1() {
		tire1.roll();
		tire2.roll();
	}

	public void run2() {
		Tire tire = new Tire(){
			@Override
			public void roll() {
				System.out.println("익명 자식 Tire 객체 2이 굴러갑니다.");
			};
		};
		tire.roll();
	}
	
	public void run3(Tire tire) {
		tire.roll();
	}
	
	public void run4(Tire tire) {
		tire.roll();
	}
	
	public void run5() {
		Tire tire = new Tire(){
			@Override
			public void roll() {
				System.out.println("익명 자식 Tire 객체 5가 굴러갑니다.");
			};
		};
		tire.roll();
	}
	
	private Tire tire5 = new Tire() {
		@Override
		public void roll() {
			System.out.println("익명 자식 Tire 객체 6이 굴러갑니다.");
		}
	};
	void run6() {
	tire5.roll();
	}
	
}
