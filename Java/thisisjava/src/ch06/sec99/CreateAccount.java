package ch06.sec99;

import java.util.Scanner;

public class CreateAccount {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int no=0;
		BankApp myBank = new BankApp();

		boolean roop = true;
		while(roop) {
			System.out.println("----------------------------------");
			System.out.println("1.계좌생성|2.계좌목록|3.예금|4.출금|5.종료");
			System.out.println("----------------------------------");


			String select = scan.nextLine();

			switch(select){
			case "1" :
				myBank.CreateAccount(no);
				no++;
				break;

			case "2" :
				myBank.AccountList();
				break;

			case "3" :
				myBank.Deposit();
				break;

			case "4" :
				myBank.Withdraw();
				break;

			case "5" :
				roop = false;
				break;

			default :
				System.out.println("올바른 값을 입력해주십시오.");
			};

		}
		scan.close();
		System.out.println("프로그램 종료");
	}
}
