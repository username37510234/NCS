package ch05.sec05;

public class SubStringExample {

	public static void main(String[] args) {
		String ssn = "880815-1234567";
		
		String firstnum = ssn.substring(0,6);
		System.out.println(firstnum);
		
		String secondnum = ssn.substring(7);
		System.out.print(secondnum);
	}

}
