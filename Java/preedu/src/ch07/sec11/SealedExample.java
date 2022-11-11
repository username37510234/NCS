package ch07.sec11;

public class SealedExample {

	public static void main(String[] args) {

		Person P = new Person();
		Employee E = new Employee();
		Manager M = new Manager();
		Director D = new Director();
		
		P.work();
		E.work();
		M.work();
		D.work();
		
		work(new Person());
		work(new Employee());
		work(new Manager());
		work(new Director());
	}
	
	public static void work(Person person) {
		person.work();
	}

}
