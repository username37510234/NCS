package ch04.sec07;

public class BreakOutterExample {

	public static void main(String[] args) throws Exception {
		Outter: for(char upper='A'; upper<='Z'; upper++) {
			for(char lower='a'; lower<='z'; lower++) {
				if(lower=='c') break;
				if(upper=='G') {
					break Outter;
				}
				System.out.println(upper + "-" +lower);
			}
		}
		System.out.print("프로그램 실행 종료");
	}

}
