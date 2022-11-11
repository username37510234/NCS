package ch05.sec09;

public class ArrayCopyExample {

	public static void main(String[] args) {
		String[] oldSA = {"java", "array", "copy"};
		String[] newSA = new String[5];
		
		System.arraycopy(oldSA, 0, newSA, 0, oldSA.length);
		
		for(int i=0; i<newSA.length;i++) {
			System.out.printf("%s, ", newSA[i]);
		}
	}

}
