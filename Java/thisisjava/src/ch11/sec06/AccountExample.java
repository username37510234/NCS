package ch11.sec06;

public class AccountExample {

	public static void main(String[] args) {
		
		Account acc = new Account();
		
		acc.deposit(20000);
		System.out.println("예금액: "+acc.getBalance());
		
		try {
			acc.withdraw(30000);
		} catch(InsufficientException e) {
			String mes = e.getMessage();
			System.out.println(mes);
		}

		System.out.println("예금액: "+acc.getBalance());
	}

}
