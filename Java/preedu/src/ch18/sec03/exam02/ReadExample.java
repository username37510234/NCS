package ch18.sec03.exam02;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

public class ReadExample {
	public static void main(String[] args) {


		try {
			InputStream is = new FileInputStream("C:/Temp/test2.db");

			byte[] dat = new byte[100];

			while(true) {
				int num = is.read(dat);
				if(num==-1)break;

				for(int i=0; i<num; i++) {
					System.out.println(dat[i]);
				}
			}

			is.close();
		} catch(FileNotFoundException e) {
			e.printStackTrace();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}
}
