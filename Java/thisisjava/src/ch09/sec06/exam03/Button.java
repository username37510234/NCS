package ch09.sec06.exam03;

public class Button {

	public static interface ClickListener{
		void onClick();
	}
	
	private ClickListener CLer;
	
	public void setClickListner(ClickListener CLer) {
		this.CLer = CLer;
	}
	
	public void click() {
		this.CLer.onClick();
	}
}
