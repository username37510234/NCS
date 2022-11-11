package ch12.sec06;

public class BoxingUnBoxingExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Integer obj = 100;
		Integer obj2 = 100;
		System.out.println("value: "+obj.intValue());
		
		
		int value = obj;
		System.out.println("value: "+value);

		boolean b = value == obj;
		System.out.println(b);
		boolean v = obj2 == obj;
		System.out.println(v);
		
		int result = obj + 100;
		System.out.println("result: "+result);
		
		
	}

}
