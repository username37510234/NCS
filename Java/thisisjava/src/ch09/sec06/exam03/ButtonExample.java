package ch09.sec06.exam03;

public class ButtonExample {

	public static void main(String[] args) {

		Button btnOk = new Button();
		
		class OkListener implements Button.ClickListener {

			@Override
			public void onClick() {
				System.out.println("Ok 버튼을 클릭했습니다.");
			}
			
		}
		
		btnOk.setClickListner(new OkListener());
		
		btnOk.click();
		
		Button btnCancel = new Button();
		
		class CancelListener implements Button.ClickListener{

			@Override
			public void onClick() {
				System.out.println("Cancel 버튼을 클릭했습니다.");
			}
			
		}
		
		btnCancel.setClickListner(new CancelListener());
		
		btnCancel.click();
	}

}
