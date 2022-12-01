package ch14.sec03.exam01;

import java.awt.Toolkit;

public class BeepPrintExample {

	public static void main(String[] args) {
		Toolkit tk = Toolkit.getDefaultToolkit();
		for(int i=0; i<5; i++) {
			tk.beep();
			try { Thread.sleep(500);} catch(Exception e) {}
		}

		for(int i=0; i<5; i++) {
			System.out.print("띵");
			try { Thread.sleep(500);} catch(Exception e) {}
		}
	}

}
