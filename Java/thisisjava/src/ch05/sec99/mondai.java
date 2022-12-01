package ch05.sec99;

import java.util.Scanner;

public class mondai {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int[] stu = {};
		int num = 0;
		int ro = 1;
		while(ro==1) {
			System.out.println("---------------------------------------------");
			System.out.println("1.학생수 | 2.점수입력 | 3.점수리스트 | 4.분석 | 5.종료");
			System.out.println("---------------------------------------------");
			System.out.print("선택>");
			String stat = scan.nextLine();
			switch(stat) {
			case "1" : System.out.print("학생수>"); num =Integer.parseInt(scan.nextLine()); stu = new int[num]; break;
			case "2" : for(int i=0;i<stu.length; i++) {
				System.out.printf("scores[%d]>",i); 
				stu[i] = Integer.parseInt(scan.nextLine());
			} break;
			case "3" : for(int i=0; i<stu.length; i++) {
				System.out.printf("scores[%d]: %d",i,stu[i]);
				System.out.println();
			} 			 break;
			case "4" : int sum = 0; int total = 0; int max = 0; for(int i=0; i<stu.length; i++) {
				sum++;
				total += stu[i];
				if(max<stu[i]) max = stu[i];
			} double avg = (double) total/sum;
			System.out.println("최고 점수: " + max);
			System.out.println("평균 점수: " + avg); break;
			case "5" : ro = 0;
			}
		}
		scan.close();
		System.out.println("프로그램 종료");
	}

}
