package ch06.sec99;

public class AccountProject {

	public static void main(String[] args) {
		Account acc1 = new Account();

		acc1.setBalance(10000);
		System.out.println("현재 잔고: "+acc1.getBalance());
		
		acc1.setBalance(-100);
		System.out.println("현재 잔고: "+acc1.getBalance());
		
		acc1.setBalance(2000000);
		System.out.println("현재 잔고: "+acc1.getBalance());
		
		acc1.setBalance(300000);
		System.out.println("현재 잔고: "+acc1.getBalance());
	}

}
