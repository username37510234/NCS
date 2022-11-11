package ch12.sec07;

import java.util.Arrays;
import java.util.Random;

public class RandomExample {

	public static void main(String[] args) {

		int[] sN = new int[6];
		Random rN = new Random();
		System.out.println("선택번호: ");
		for(int i=0; i<6; i++) {
			sN[i] = rN.nextInt(45) +1;
			System.out.print(sN[i]+" ");
		}
		System.out.println();
		
		int[] wN = new int[6];
		rN = new Random();
		System.out.println("당첨번호: ");
		for(int i=0; i<6; i++) {
			wN[i] = rN.nextInt(45) +1;
			System.out.print(wN[i]+" ");
		}
		System.out.println();

		Arrays.sort(sN);
		Arrays.sort(wN);
		boolean result = Arrays.equals(sN, wN);
		System.out.println("당첨여부: ");
		if(result) {
			System.out.println("1등에 당첨되셨습니다.");
		} else {
			System.out.println("꽝");
		}
	}

}
