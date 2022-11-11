package ch18.sec99;

import java.io.BufferedReader;
import java.io.FileReader;

public class Example {

	public static void main(String[] args) throws Exception {

		String filePath = "C:/ThisisJavaSecondEdition/workspace/thisisjava/src/ch02/sec01/VariableUseExample.java";
		
		FileReader fr = new FileReader(filePath);
		BufferedReader br = new BufferedReader(fr);
		
		int rowN = 0;
		String rowD;
		while(true) {
			rowD = br.readLine();
			if(rowD == null)break;
			System.out.printf("%d: %s \n", ++rowN, rowD);
			
		}
		
		br.close();
		fr.close();
	}

}
