package ch05.sec08;

public class ArrayReferenceObjetExample {

	public static void main(String[] args) {
		String[] strA = new String[3];
		strA[0] = "Java";
		strA[1] = "Java";
		strA[2] = new String("Java");

		System.out.println(strA[0] == strA[1]);
		System.out.println(strA[0] == strA[2]);
		System.out.println(strA[0].equals(strA[2]));
	}

}
