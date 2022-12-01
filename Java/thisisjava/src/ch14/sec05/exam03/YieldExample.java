package ch14.sec05.exam03;

public class YieldExample {

	public static void main(String[] args) {
		
		WorkThread wTA = new WorkThread("workThreadA");
		WorkThread wTB = new WorkThread("workThreadB");
		wTA.start();
		wTB.start();
		
		try {Thread.sleep(5000);}catch (InterruptedException e) {}
		wTA.work = false;
		
		try {Thread.sleep(10000);}catch (InterruptedException e) {}
		wTA.work = true;
	}

}
