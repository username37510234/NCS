package ch19.sec03.exam01;

import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class ClientExample {
	public static void main(String[] args) {
		try {
			Socket soc = new Socket("localhost",50001);
			System.out.println("[클라이언트] 연결 성공");
			
			soc.close();
			System.out.println("[클라이언트] 연결 끊음");
		} catch (UnknownHostException e) {}
		catch(IOException e) {}
	} 
}
