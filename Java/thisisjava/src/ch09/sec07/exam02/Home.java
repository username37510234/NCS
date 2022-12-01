package ch09.sec07.exam02;

public class Home {

	private RemoteControl rc = new RemoteControl() {
		
		@Override
		public void turnON() {
			System.out.println("TV를 켭니다");
		}
		
		@Override
		public void turnOFF() {
			System.out.println("TV를 끕니다");			
		}
	};
	
	public void use1() {
		rc.turnON();
		rc.turnOFF();
	}
	
	public void use2() {
		RemoteControl rc = new RemoteControl() {
			
			@Override
			public void turnON() {
			System.out.println("에어컨을 켭니다.");	
			}
			
			@Override
			public void turnOFF() {
				System.out.println("에어컨을 끕니다.");	
			}
		};
		rc.turnON();
		rc.turnOFF();
	}
	
	public void use3(RemoteControl rc) {
		rc.turnON();
		rc.turnOFF();
	}
}
