package ch19.sec03.exam02;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class EchoClient {

	public static void main(String[] args) {
		try {
			Socket soc = new Socket("localhost",16860);
			System.out.println("[클라이언트] 연결 성공");
			
			String sendM = "나는 자바가 좋아~~";
			DataOutputStream dos = new DataOutputStream(soc.getOutputStream());
			dos.writeUTF(sendM);
			dos.flush();
			System.out.println("[클라이언트] 데이터 보냄: "+sendM);
			
			DataInputStream dis = new DataInputStream(soc.getInputStream());
			String receiveM = dis.readUTF();
			System.out.println("[클라이언트] 데이터 받음: "+receiveM);
			
			
			soc.close();
			System.out.println("[클라이언트] 연결 끊음");
		} catch (UnknownHostException e) {}
		catch(IOException e) {}
	}

}
