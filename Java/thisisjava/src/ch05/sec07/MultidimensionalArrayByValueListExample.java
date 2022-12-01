package ch05.sec07;

public class MultidimensionalArrayByValueListExample {

	public static void main(String[] args) {
		int[][] scores = {
				{80,90,96},
				{76,88}
		};

		System.out.println("1차원 배열 길이(반의 수): "+scores.length);
		System.out.println("2차원 배열 길이(첫 번째 반의 학생 수): "+scores[0].length);
		System.out.println("2차원 배열 길이(두 번째 반의 학생 수): "+scores[1].length);
		
		System.out.println("scores[0][2]: "+scores[0][2]);
		System.out.println("scores[1][1]: "+scores[1][1]);
		
		int c1sum = 0;
		int c2sum=0;
		int tsum=0;
		int ts=0;
		for(int k=0;k<scores.length; k++) {
			for(int i=0;i<scores[k].length; i++) {
				if (k==0) c1sum += scores[k][i];
				else if (k==1) c2sum += scores[k][i];
				tsum += scores[k][i];
			}
			ts += scores[k].length;
		}
		double c1avg = (double)c1sum/scores[0].length;
		double c2avg = (double)c2sum/scores[1].length;
		double tavg = (double)tsum/ts;
		System.out.println("첫 번째 반의 평균 점수: "+c1avg);
		System.out.println("첫 번째 반의 평균 점수: "+c2avg);
		System.out.println("전체 학생의 평균 점수: "+tavg);
	}

}
