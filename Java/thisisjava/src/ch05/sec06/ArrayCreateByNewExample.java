package ch05.sec06;

public class ArrayCreateByNewExample {

	public static void main(String[] args) {
		int[] arr1 = new int[3];
		
		for(int i=0; i<arr1.length; i++) {
			System.out.printf("arr1[%d] : %d, ",i,arr1[i]);
		}
		System.out.println();
		
		for(int i=0; i<arr1.length; i++) {
			arr1[i] = (i+1)*10;
		}
		for(int i=0; i<arr1.length; i++) {
			System.out.printf("arr1[%d] : %d, ",i,arr1[i]);
		}
		System.out.println("\n");
		
		double[] arr2 = new double[3];
		
		for(int i=0; i<arr2.length; i++) {
			System.out.printf("arr2[%d] : %.1f, ",i,arr2[i]);
		}
		System.out.println();
		
		for(int i=0; i<arr2.length; i++) {
			arr2[i] = (i+1)*0.1;
		}
		for(int i=0; i<arr2.length; i++) {
			System.out.printf("arr2[%d] : %.1f, ",i,arr2[i]);
		}
		System.out.println("\n");
		
		String[] arr3 = new String[12];
		for(int i=0; i<arr3.length; i++) {
			System.out.printf("arr3[%d] : %s, ",i,arr3[i]);
		}
		System.out.println();
		
		for(int i=0; i<arr3.length; i++) {
			arr3[i] = (i+1)+"월";
			System.out.printf("arr3[%d] : %s, ",i,arr3[i]);
		}
	}

}
