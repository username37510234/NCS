package ch05.sec08;

public class ArrayReferenceObjectExample {

	public static void main(String[] args) {
		String[] strarray = new String[3];
		strarray[0] = "Java";
		strarray[1] = "Java";
		strarray[2] = new String("Java");
		
		System.out.println( strarray[0] == strarray[1]);
		System.out.println( strarray[0] == strarray[2]);
		System.out.println( strarray[0].equals(strarray[1]));
		
	}

}
