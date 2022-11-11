package ch05.sec07;

public class MultidimensionalArrayByNewExample {

	public static void main(String[] args) {
		int[][] mathscores = new int[2][3];
		for(int i=0; i< mathscores.length; i++) {
			for (int j=0; j<mathscores[i].length; j++){
				System.out.printf("mathscores[%d][%d]: %d\t",i,j,mathscores[i][j]);
			}
		}
		System.out.println();
		
		for(int i=0;i<mathscores.length;i++) {
			for(int j=0;j<mathscores[i].length;j++) {
				mathscores[i][j] = (int)(Math.random()*21) +80;
//				System.out.println(mathscores[i][j]);
			}
		}
		int totalstudent = 0;
		int totalmathsum = 0;
		for(int i=0;i<mathscores.length;i++) {
			for(int j=0;j<mathscores[i].length;j++) {
				totalstudent++;
//				System.out.print(totalstudent);
				totalmathsum += mathscores[i][j];
			}
		}
		
		double totalmathavg = (double) totalmathsum/totalstudent;
		System.out.println("전체 학생의 수학 평균 점수: "+totalmathavg);
		System.out.println();
		
		int[][] englishscores = new int[2][];
		englishscores[0] = new int[2];
		englishscores[1] = new int[3];
		for (int i=0; i<englishscores.length; i++) {
			for(int j=0;j<englishscores[i].length; j++) {
				System.out.printf("englishscores[%d][%d]: %d\t",i,j,englishscores[i][j]);
			}
		}
		System.out.println();

		for(int i=0;i<englishscores.length;i++) {
			for(int j=0;j<englishscores[i].length;j++) {
				englishscores[i][j] = (int)(Math.random()*21) +80;
//				System.out.println(englishscores[i][j]);
			}
		}
		int totalestudent = 0;
		int totalenglishsum = 0;
		for(int i=0;i<englishscores.length;i++) {
			for(int j=0; j<englishscores[i].length;j++) {
				totalestudent++;
				totalenglishsum += englishscores[i][j];
			}
		}
		double totaleavg = (double) totalenglishsum / totalestudent;
		System.out.print("전체 학생의 영어 평균 점수: "+ totaleavg);
		
	}
}
