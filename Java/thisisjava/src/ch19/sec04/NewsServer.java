package ch19.sec04;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketAddress;
import java.util.Scanner;

public class NewsServer {

	private static DatagramSocket datagramsocket = null;

	public static void main(String[] args) throws Exception {

		System.out.println("------------------------------------------------");
		System.out.println("서버를 종료하려면 q 또는 Q를 입력하고 Enter 키를 입력하세요.");
		System.out.println("------------------------------------------------");

		startServer();

		Scanner scan = new Scanner(System.in);
		while (true) {
			String key = scan.nextLine();
			if (key.toLowerCase().equals("q"))
				break;
		}

		scan.close();

		stopServer();
	}

	public static void startServer() {
		Thread thread = new Thread() {
			@Override
			public void run() {
				try {
					datagramsocket = new DatagramSocket(16860);
					System.out.println("[서버] 시작됨");

					while (true) {
						DatagramPacket receivePacket = new DatagramPacket(new byte[1024], 1024);
						datagramsocket.receive(receivePacket);
						String newsKind = new String(receivePacket.getData(), 0, receivePacket.getLength(), "UTF-8");

						SocketAddress socketAddress = receivePacket.getSocketAddress();

						for (int i = 1; i <= 10; i++) {
							String data = newsKind + ": 뉴스" + i;
							byte[] bytes = data.getBytes("UTF-8");
							DatagramPacket sendPacket = new DatagramPacket(bytes, 0, bytes.length, socketAddress);
							datagramsocket.send(sendPacket);
						}
					}
				} catch (IOException e) {
					System.out.println("[서버]" + e.getMessage());
				}
			}
		};

		thread.start();
	}

	public static void stopServer() {
		datagramsocket.close();
		System.out.println("[서버] 종료됨");
	}
}
