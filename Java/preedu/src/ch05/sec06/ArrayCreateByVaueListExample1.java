package ch05.sec06;

public class ArrayCreateByVaueListExample1 {

	public static void main(String[] args) {
		//배열 변수 선언과 배열 생성
		String[] season = { "Spring" , "Summer" , "Fall" , "Winter" };
		
		//배열의 항목값 읽기
		for(int i=0; i<=3; i++) {
			System.out.printf("season[%d] : %s\n", i , season[i]);
		}
		
		//인덱스 1번 항목의 값 변경
		season[1] = "여름";
		System.out.println("season[1] : "+season[1]);
		System.out.println();
		
		//배열 변수 선언과 배열 생성
		int[] scores = { 83, 90, 87 };
		
		//총합과 평균 구하기
		int sum=0;
		for(int i=0;i<3;i++) {
			sum += scores[i];
		}
		System.out.println("총합 : "+sum);
		double avg = (double) sum / 3;
		System.out.print("평균 : "+avg);
		
	}

}
