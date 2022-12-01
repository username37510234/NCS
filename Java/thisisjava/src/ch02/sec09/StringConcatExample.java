package ch02.sec09;

public class StringConcatExample {

	public static void main(String[] args) {
		int result1 = 10 + 2+ 8;
		System.out.println("result1: "+result1);

		String result2 = 10 + 2+ "8";
		System.out.println("result2: "+result2);

		result2 = 10 + "2"+ 8;
		System.out.println("result3: "+result2);

		result2 = "10" + 2+ 8;
		System.out.println("result4: "+result2);

		result2 = "10" + (2+ 8);
		System.out.println("result5: "+result2);
		
	}

}
