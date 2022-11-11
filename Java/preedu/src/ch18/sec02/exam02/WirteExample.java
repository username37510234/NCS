package ch18.sec02.exam02;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class WirteExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		try {
			OutputStream os = new FileOutputStream("C:/Temp/test2.db");
			
			byte[] array = {10, 20, 30};
			
			os.write(array);
			
			os.flush();
			os.close();
			
		}catch(IOException e) {
			e.printStackTrace();
		}
	}

}
