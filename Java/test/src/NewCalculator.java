import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenuBar;
import javax.swing.JPanel;
import javax.swing.JTextField;

class NewCalculator implements ActionListener {


	JTextField textField;
	JTextField textfieldNorth;

	JFrame frame;
	JMenuBar menubar;
	GridLayout grid;
	JButton Bu;
	JPanel panel1;
	JPanel panelNorth;
	String[] strGrid= {"7","8","9","+","6","5","4","-","3","2","1","*","0","=","%","/"};

	private String count = ""; // 초기값
	int num = 0;   //저장된 숫자
	private String comb = ""; // 저장된 명령어

	public NewCalculator() {

		frame = new JFrame("계산기 예제");
		menubar = new JMenuBar();

		panel1 = new JPanel();
		panelNorth=new JPanel();
		textField=new JTextField("0");
		textfieldNorth=new JTextField("");  
	}

	public void gui() {

		textField.setHorizontalAlignment(JTextField.RIGHT);
		textField.setEditable(false);

		textfieldNorth.setHorizontalAlignment(JTextField.RIGHT);
		textfieldNorth.setEditable(false);

		panelNorth.setLayout(new BorderLayout());
		panelNorth.add(BorderLayout.NORTH,textfieldNorth);
		panelNorth.add(BorderLayout.CENTER,textField);

		panel1.setLayout(new GridLayout(4,3,6,6));
		panel1.setBackground(new Color(222,232,244));

		for(int i=0; i<strGrid.length; i++){
			Bu=new JButton(strGrid[i]);  			
			Bu.addActionListener(this);	 		
			Bu.setBackground(new Color(241,244,249));  
			panel1.add(Bu); 						
		}

		frame.add(BorderLayout.NORTH,panelNorth);
		frame.add(BorderLayout.CENTER,panel1);
		frame.setJMenuBar(menubar);  
		frame.setSize(280,360);  
		frame.setVisible(true);    
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 

	}

	public void actionPerformed(ActionEvent e) {
		String str = e.getActionCommand();
		String read;
		try {
			if(str!="/" && str!="*" && str!="+" && str!="-" && str!="=" && str!="%") {
			    
				textField.setText(count);
				textField.getText();
//				textfieldNorth.setText("");
				textfieldNorth.getText();
				

				read = textField.getText();
				count = read + str;
				if(count.startsWith("0")) {count = count.substring(1);} // 000 제거
				textField.setText(count);
				textField.getText();
			}

			if(str=="/" || str=="*" || str=="+" || str=="-" || str=="%") {

                if(comb!="") {logic();}
				textfieldNorth.setText(count+" "+str);
				textfieldNorth.getText();

				num = Integer.parseInt(count);
				count = "";
				comb = str;
			}
/*
			if(str=="C") {
				textfieldNorth.setText("");
				textfieldNorth.getText();
				count = "";
				read = "";
				comb = "";
				num = 0;
				textField.setText("0");
				textField.getText();
			}
*/ // 초기화 제거
			if(str=="=") {
			    if (comb!="") {// 수식이 입력되지 않으면 아무행동 않도록
				logic();
				comb = "";
				textField.setText(count);
				textField.getText();
			    } else {} 
			}

		} catch(Exception e1) {
			textField.setText("Error.");
			textField.getText(); 
			textfieldNorth.setText("");
            comb = "";
            count = ""; // 에러시 초기화
		}
	}
	public static void main(String[] args) {
		NewCalculator traC=new NewCalculator();
		traC.gui();
	}

	public void logic() {
	    int sigh = Integer.parseInt(textField.getText());
        int result = 0;
	    switch (comb) {
            case "+" : result = num+sigh;break;
            case "-" : result = num-sigh;break;
            case "*" : try{result = num*sigh;}catch(Exception exc){result=0;}break;
            case "/" : try{result = num/sigh;}catch(Exception exc){result=0;}break;
            case "%" : try{result = num%sigh;}catch(Exception exc){result=0;}break;
            }
        textfieldNorth.setText(num+" "+comb+" "+count+" =");
        textfieldNorth.getText();
        count = String.valueOf(result);
        num = result;
	} // 실질적인 계산부분


}
