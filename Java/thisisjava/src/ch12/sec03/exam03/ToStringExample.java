package ch12.sec03.exam03;

public class ToStringExample {

	public static void main(String[] args) {
		
		SmartPhone myP = new SmartPhone("삼성전자", "안드로이드");
		
		String strObj = myP.toString();
		System.out.println(strObj);
		
		System.out.println(myP);
	}

}
