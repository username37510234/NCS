package ch08.sec13;

public class SealedExample {

	public static void main(String[] args) {
		implClass impl = new implClass();
		
		InterFaceA ia = impl;
		ia.methodA();
		
		System.out.println();
		
		InterFaceB ib = impl;
		ib.methodA();
		ib.methodB();
		
		System.out.println();
		
		InterFaceC ic = impl;
		ic.methodA();
		ic.methodB();
		ic.methodC();
	}

}
