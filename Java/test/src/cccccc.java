import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

// ***** 클래스명 변경
class cccccc  implements ActionListener
{	
	JFrame frame;     //JFrame 변수 선언   
	JTextField textfieldNorth; 
	JTextField textField;
	JMenuBar menuBar;
	//	JMenu menu;   //***** 메뉴제거
	//	JMenu menu2;  //***** 메뉴제거
	//	JMenu menu3;  //***** 메뉴제거
	JPanel panel1;  //Border 
	JPanel panelNorth;  //Border 
	GridLayout grid;
	JButton JBu;
	String[] strGrid= {"7","8","9","+","6","5","4","-","3","2","1","*","0","C","=","/"};

	private String count = "";
	int num = 0;
	private String comb = "";


	public cccccc(){
		//frame=new JFrame("계산기"); // ***** 타이틀 '계산기 예제'로 변경
		frame=new JFrame("계산기예제zz");
		menuBar=new JMenuBar();

		// ***** 메뉴제거
		//		menu=new JMenu("보기(V)");
		//		menu.setFont(new Font("Sans-serif", 0, 12));
		//		
		//		menu2=new JMenu("편집(E)");
		//		menu2.setFont(new Font("Sans-serif", 0, 12));
		//		
		//		menu3=new JMenu("도움말(H)");
		//		menu3.setFont(new Font("Sans-serif", 0, 12));

		panel1=new JPanel();
		panelNorth=new JPanel();
		textField=new JTextField("0"); 			// 초기값 아무것도 안보이게
		textfieldNorth=new JTextField(""); 		// 연산자만 보이는 텍스트 
	}// 생성자 NewCalculator()


	public void gui(){
		// ***** 메뉴제거
		//		menuBar.add(menu);		// 메뉴바에 메뉴들 1,2,3 붙였다 
		//		menuBar.add(menu2);	
		//		menuBar.add(menu3);	

		textField.setHorizontalAlignment(JTextField.RIGHT);   // 우측정렬
		textField.setEditable(false); 		// 텍스트필드창에 텍스트쓰지못하게 잠금

		textfieldNorth.setHorizontalAlignment(JTextField.RIGHT);  // 우측정렬
		textfieldNorth.setEditable(false); 	// 텍스트필드창에 텍스트쓰지못하게 잠금

		panelNorth.setLayout(new BorderLayout());    		// 레이아웃 설정.
		panelNorth.add(BorderLayout.NORTH,textfieldNorth);   // 패널에 텍스트필드를 두개 붙임.
		panelNorth.add(BorderLayout.CENTER,textField);

		panel1.setLayout(new GridLayout(4,3,6,6));  		// 그리드 레이아웃 속성설정
		panel1.setBackground(new Color( 222,232,244));  // 패널색상


		for(int i=0; i<strGrid.length; i++){
			JBu=new JButton(strGrid[i]);  				// 버튼 생성 
			JBu.addActionListener(this);	 			// 각 버튼마다 리스너 붙이기
			JBu.setBackground(new Color( 241,244,249));    // 버튼 집어넣기
			panel1.add(JBu); 							// 패널에 각각의 버튼들 붙이기
		}


		frame.add(BorderLayout.NORTH,panelNorth); 
		frame.add(BorderLayout.CENTER,panel1); 		 // 텍스트필드 북쪽에
		frame.setJMenuBar(menuBar);  				// 메뉴바 붙이기

		frame.setResizable(false);                                  //창 크기 변경 못하게 막는다.
		// ***** 창의 크기변경 "계산기 예제가 다 보이면 될 사이즈로 변경
		//frame.setSize(220,310);                                    //frame 의 크기  
		frame.setSize(260,310);                                    //frame 의 크기		
		frame.setVisible(true);                                   //frame을 화면에 나타나도록 설정
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);    //X버튼 활성화 
	}//gui()


	public void actionPerformed(ActionEvent e){
		String str=e.getActionCommand();  		// 문자열로 이벤트불러옴
		String read;				// 텍스트필드에 있는 텍스트 읽기용도

		try {
			if(str!="/" && str!="*" && str!="+" && str!="-" && str!="=" && str!="C") {
				textField.setText(count);
				textField.getText();
				textfieldNorth.getText();

				read = textField.getText();
				count = read + str;
				textField.setText(count);
				textField.getText();
			}

			if(str=="/" || str=="*" || str=="+" || str=="-") {

				textfieldNorth.setText(count+" "+str);
				textfieldNorth.getText();

				num = Integer.parseInt(count);
				count = "";
				comb = str;
			}

			if(str=="C") {
				textfieldNorth.setText("");
				count = "";
				read = "";
				comb = "";
				num = 0;
				textField.setText("0");
				textField.getText();
			}

			if(str=="=") {
				int sigh = Integer.parseInt(textField.getText());
				int result=0;
				switch (comb) {
				case "+" : result = num+sigh;break;
				case "-" : result = num-sigh;break;
				case "*" : try{result = num*sigh;}catch(Exception exc){result=0;}break;
				case "/" : try{result = num/sigh;}catch(Exception exc){result=0;}break;
				}
				textfieldNorth.setText(num+" "+comb+" "+count+" =");
				textfieldNorth.getText();
				count = String.valueOf(result);
				num = result;
				textField.setText(count);
				textField.getText();
			}

		} catch(Exception e1) {
			textField.setText("Error 다시입력 C클릭.");
			textField.getText(); 
		}
	}



	public static void main(String[] args) 
	{
		// ***** 클래스명 변경
		cccccc cal=new cccccc();
		cal.gui();
	}// main()
}// class
