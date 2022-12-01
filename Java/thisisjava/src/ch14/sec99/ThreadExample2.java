package ch14.sec99;

public class ThreadExample2 {

	public static void main(String[] args) {
		Thread thread = new MovieThread2();
		thread.start();
		
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
		}
		
		thread.interrupt();
		System.out.println("동영상을 종료합니다.");
	}

}
