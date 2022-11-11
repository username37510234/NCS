package ch18.sec07.exam01;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

public class BufferExample {

	public static void main(String[] args) throws Exception {
		
		String oFP1 = BufferExample.class.getResource("originalFile1.jpg").getPath();
		String tFP1 = "C:/Temp/targetFile1.jpg";
		FileInputStream fis = new FileInputStream(oFP1);
		FileOutputStream fos = new FileOutputStream(tFP1);
		
		String oFP2 = BufferExample.class.getResource("originalFile2.jpg").getPath();
		String tFP2 = "C:/Temp/targetFile2.jpg";
		FileInputStream fis2 = new FileInputStream(oFP2);
		FileOutputStream fos2 = new FileOutputStream(tFP2);
		BufferedInputStream bis = new BufferedInputStream(fis2);
		BufferedOutputStream bos = new BufferedOutputStream(fos2);
		
		long nBT = copy(fis, fos);
		System.out.println("버퍼 미사용:\t"+ nBT + " ns");
		
		long bT = copy(bis,bos);
		System.out.println("버퍼 사용:\t\t"+ bT + " ns");
		
		fis.close();
		fos.close();
		bis.close();
		bos.close();
	}

	public static long copy(InputStream is,OutputStream os) throws Exception{
		long start = System.nanoTime();
		
		while(true) {
			int data = is.read();
			if(data == -1) break;
			os.write(data);
		}
		os.flush();
		long end = System.nanoTime();
		return (end-start);
	}
}
