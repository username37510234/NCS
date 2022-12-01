package ch04.sec04;

public class MultiplicationTableExample {

	public static void main(String[] args) {
		for(int m=2;m<=9;m++) {
			System.out.println("\n*** "+m+"단 ***");
			for(int n=1;n<=9;n++) {
				System.out.printf("%d x %d = %2d\n", m,n,(m*n));
			}
		}
	}

}
