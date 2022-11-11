package ch05.sec10;

public class AdvancedForExample {

	public static void main(String[] args) {
		int[] scs = {95,71,84,93,87};
		
		int sum= 0;
		for(int sc : scs) {
			sum += sc;
		}
		System.out.println("점수 총합 = "+sum);
		double avg = (double)sum/scs.length;
		System.out.println("점수 평균 = "+avg);
	}

}
