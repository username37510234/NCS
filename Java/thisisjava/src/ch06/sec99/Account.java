package ch06.sec99;

public class Account {

	private int balance;
	public static int MIN_BALANCE = 0;
	public static int MAX_BALANCE = 1000000;

	public int getBalance() {
		return balance;
	}

	public void setBalance(int balance) {
		if( balance<Account.MIN_BALANCE) {
			return;
		} else if (balance>Account.MAX_BALANCE){
			return;
		}
		this.balance = balance;
	}
	
	
}
