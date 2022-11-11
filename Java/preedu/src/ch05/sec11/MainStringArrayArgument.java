package ch05.sec11;

public class MainStringArrayArgument {

	public static void main(String[] args) {
		if(args.length!=2) {
			System.out.println("프로그램 입력값이 부족");
			System.exit(0);
		}
		
		String strnum1 = args[0];
		String strnum2 = args[1];
		int num1 = Integer.parseInt(strnum1);
		int num2 = Integer.parseInt(strnum2);
		
		int result = num1 + num2;
		System.out.printf("%d + %d = %d",num1,num2,result);
	}

}
