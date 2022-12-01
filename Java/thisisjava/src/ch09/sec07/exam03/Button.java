package ch09.sec07.exam03;

public class Button {

	public static interface ClickListener{
		void onClick();
	}
	
	private ClickListener CLer;
	
		
	public void setCLer(ClickListener cLer) {
		CLer = cLer;
	}

	public void click() {
		this.CLer.onClick();
	}
}
