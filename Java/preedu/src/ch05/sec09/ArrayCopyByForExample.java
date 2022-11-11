package ch05.sec09;

public class ArrayCopyByForExample {

	public static void main(String[] args) {
		int[] oldIA = {1,2,3};
		int[] newIA = new int[5];
		
		for(int i=0; i<oldIA.length; i++) {
			newIA[i] = oldIA[i];
		}
		for(int i=0; i<newIA.length; i++) {
			System.out.print(newIA[i]+", ");
		}
	}

}
