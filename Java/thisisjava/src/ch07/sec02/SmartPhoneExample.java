package ch07.sec02;

public class SmartPhoneExample {

	public static void main(String[] args) {
		SmartPhone myP = new SmartPhone("갤럭시","은하");

		System.out.println("모델: "+myP.model);
		System.out.println("색상: "+myP.color);
		
		System.out.println("와이파이 상태: "+myP.wifi);
		
		myP.bell();
		myP.sendVoice("여보세요.");
		myP.receiveVoice("안녕하세요! 저는 홍길동인데요.");
		myP.sendVoice("아~ 네. 반갑습니다.");
		myP.hangUp();
		
		myP.setWifi(true);
		myP.interent();
	}

}
