package ch14.sec04;

public class ThreadNameExample {

	public static void main(String[] args) {
		
		Thread mT = Thread.currentThread();
		System.out.println(mT.getName());
		
		for(int i=0;i<3; i++) {
			Thread tA = new Thread() {
				@Override
				public void run() {
					System.out.println(getName()+" 실행");;
				}
			};
			tA.start();
		}
		
		Thread cT = new Thread() {
			@Override
			public void run() {
				System.out.println(getName()+" 실행");;
			}
		};
		cT.setName("chat-thread");
		cT.start();
	}

}
