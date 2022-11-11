package ch05.sec06;

public class ArrayCreateByNewExample {

	public static void main(String[] args) {
		//배열 변수 선언과 배열 생성
		int[] arr1 = new int[3];
		//배열 항목의 초기값 출력
		for(int i=0; i<3; i++) {
			System.out.print("arr1["+i+"] : "+arr1[i]+", ");
		}
		System.out.println();
		//배열 항목의 값 변경
		for(int i=1; i<4; i++) {
			arr1[i-1] = i*10;
		}
		//배열 항목의 변경 값 출력
		for(int i=0; i<3; i++) {
			System.out.printf("arr1[%d] : %d ",i,arr1[i]);
		}
		System.out.println("\n");
		
		//배열 변수 선언과 배열 생성
		double[] arr2 = new double[3];
		//배열 항목의 초기값 출력
		for(int i=0; i<3; i++) {
			System.out.printf("arr1[%d] : %.1f, ", i, arr2[i]);
		}
		System.out.println();
		//배열 항목의 값 변경
		for(int i=1; i<4; i++) {
			arr2[i-1] = i*0.1;
		}
		//배열 항목의 변경 값 출력
		for(int i=0;i<3;i++) {
			System.out.printf("arr2[%d] : %.1f, ", i, arr2[i]);
		}
		System.out.println("\n");
		
		//배열 변수 선언과 배열 생성
		String[] arr3 = new String[3];
		//배열 항목의 초기값 출력
		for(int i=0; i<3; i++) {
			System.out.printf("arr3[%d] : %s, ",i , arr3[i]);
		}
		System.out.println();
		//배열 항목의 값 변경
		for(int i=0; i<3; i++) {
			arr3[i] = (i+1)+"월";
		//배열 항목의 변경값 출력
			System.out.printf("arr3[%d] : %s, ", i, arr3[i]);
		}
	}

}
