package ch14.sec05.exam02;

public class joinExample {

	public static void main(String[] args) {
		SumThread sT = new SumThread();
		sT.start();
		try {
			sT.join();
		} catch (InterruptedException e) {}
		System.out.println("1~100 합: "+ sT.getSum());
	}

}
