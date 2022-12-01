package ch04.sec02;

public class IfNestedExample {

	public static void main(String[] args) {
		int score = (int)(Math.random()*20)+81;
		System.out.println("점수: " + score);
		
		String grade;
		
		if(score>=90) {
			if(score>=95) {
				grade = "A+";
			} else {	//90 이상 95미만
				grade = "A";
			}
		} else {	//90미만
			if(score>=85) {
				grade = "B+";
			} else {	//85미만
				grade = "B";
			}
		}
		
		System.out.print("학점: " + grade);
	}

}
