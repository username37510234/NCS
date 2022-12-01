package ch14.sec03.exam03;

import java.awt.Toolkit;

public class BeepPrintExample {

	public static void main(String[] args) {
		Thread thread = new Thread() {

			@Override
			public void run() {
				Toolkit tk = Toolkit.getDefaultToolkit();
				for(int i=0; i<5; i++) {
					tk.beep();
					System.out.print("진");
					try { Thread.sleep(500);} catch(Exception e) {}
				}
			}
		};
		
		thread.start();

		for(int i=0; i<5; i++) {
			System.out.print("띵");
			try { Thread.sleep(532);} catch(Exception e) {}
		}
	}

}
