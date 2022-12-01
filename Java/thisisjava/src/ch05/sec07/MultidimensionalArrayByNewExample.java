package ch05.sec07;

public class MultidimensionalArrayByNewExample {

	public static void main(String[] args) {
		int[][] mathS = new int[2][3];
		
		for(int i=0;i<mathS.length; i++) {
			for(int k=0;k<mathS[i].length; k++) {
				System.out.printf("mathS[%d][%d]: %d, ",i,k,mathS[i][k]);
			}
		}
		System.out.println();
		
		for(int i=0;i<mathS.length;i++) {
			for(int j=0;j<mathS[i].length;j++) {
				mathS[i][j] = ((int)Math.random()*20) + 81;
			}
		}
		int tStu = 0;
		int tMSum = 0;
		for(int i=0; i<mathS.length; i++) {
			for(int j=0; j<mathS.length; j++) {
				tMSum += mathS[i][j];
			}
			tStu += mathS[i].length;
		}
		double tMAvg = (double) tMSum / tStu;
		System.out.println("전체 학생의 수학 평균 점수: "+tMAvg);
		System.out.println();
		
		int[][] engS = new int[2][];
		engS[0] = new int[2];
		engS[1] = new int[3];
		for (int i=0; i<engS.length; i++) {
			for (int j=0; j<engS[i].length; j++) {
				System.out.printf("engS[%d][%d]: %d, ",i,j,engS[i][j]);
				engS[i][j] = ((int)Math.random()*20)+81;
			}
		}
		System.out.println();
		
		tStu = 0;
		int tESum = 0;
		for (int i=0; i<engS.length; i++) {
			tStu += engS[i].length;
			for (int j=0; j<engS[i].length; j++) {
				tESum += engS[i][j];
			}
		}
		
		double tEAvg = (double)tESum / tStu;
		System.out.println("전체 학생의 영어 평균 점수: "+tEAvg);
	}

}
