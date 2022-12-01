package ch08.sec09;

public class ExtendsExample {

	public static void main(String[] args) {
		InterfaceCImpl imp = new InterfaceCImpl();
		
		InterfaceA ia = imp;
		ia.methodA();
		System.out.println();
		
		InterfaceB ib = imp;
		ib.methodB();
		System.out.println();
		
		InterfaceC ic = imp;
		ic.methodA();
		ic.methodB();
		ic.methodC();
		System.out.println();
		
		imp.methodA();
		imp.methodB();
		imp.methodC();
		
	}

}
