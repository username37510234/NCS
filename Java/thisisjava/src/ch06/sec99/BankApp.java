package ch06.sec99;

import java.util.Scanner;

public class BankApp {
	Scanner scan = new Scanner(System.in);
	String[][] AccountFile = new String[100][3];

	void CreateAccount(int no) {
		System.out.println("----------");
		System.out.println("계좌생성");
		System.out.println("----------");
		System.out.print("계좌번호: ");
		AccountFile[no][0] = scan.nextLine();
		System.out.print("계좌주: ");
		AccountFile[no][1] = scan.nextLine();
		System.out.print("초기입금액: ");
		AccountFile[no][2] = scan.nextLine();
		System.out.println("결과: 계좌가 생성되었습니다.");
	}

	void AccountList() {
		System.out.println("----------");
		System.out.println("계좌목록");
		System.out.println("----------");
		for(int i=0; AccountFile[i][0]!=null; i++) {
			System.out.printf("%s\t\t%s\t%s\n",AccountFile[i][0],AccountFile[i][1],AccountFile[i][2]);
		}
	}

	void Deposit() {
		System.out.println("----------");
		System.out.println("예금");
		System.out.println("----------");
		System.out.print("계좌번호: ");
		String no = scan.nextLine();
		for(int i=0; AccountFile[i][0]!=null; i++) {
			if(AccountFile[i][0].equals(no)) {
				System.out.print("예금액: ");
				int plus = Integer.parseInt(scan.nextLine());
				AccountFile[i][2] = String.valueOf(Integer.parseInt(AccountFile[i][2]) + plus);
				return;
			} 
		}
		System.out.println("잘못된 계좌번호입니다.");
	}

	void Withdraw() {
		System.out.println("----------");
		System.out.println("출금");
		System.out.println("----------");
		System.out.print("계좌번호: ");
		String no = scan.nextLine();
		for(int i=0; AccountFile[i][0]!=null; i++) {
			if(AccountFile[i][0].equals(no)) {
				System.out.print("출금액: ");
				int minus = Integer.parseInt(scan.nextLine());
				if (minus>Integer.parseInt(AccountFile[i][2])) {
					System.out.println("출금 불가능한 금액입니다.");
					return;
				}
				AccountFile[i][2] = String.valueOf(Integer.parseInt(AccountFile[i][2]) - minus);
				System.out.println("결과: 출금이 성공되었습니다.");
				return;
			} 
		}
		System.out.println("잘못된 계좌번호입니다.");
	}
}
