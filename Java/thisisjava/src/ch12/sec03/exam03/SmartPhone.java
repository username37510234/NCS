package ch12.sec03.exam03;

public class SmartPhone {

	private String company;
	private String os;
	
	public SmartPhone(String company,String os) {
		this.company = company;
		this.os = os;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return company + ", " + os;
	}
	
}
