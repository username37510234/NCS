package ch14.sec99;

public class ThreadExample3 {

	public static void main(String[] args) {
		Thread thread = new MovieThread3();
		thread.setDaemon(true);
		thread.start();
		
		try {Thread.sleep(3000);} catch(InterruptedException e) {}
	}

}
