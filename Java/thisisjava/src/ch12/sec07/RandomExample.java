package ch12.sec07;

import java.util.Arrays;
import java.util.Random;

public class RandomExample {

	public static void main(String[] args) {
		
		int[] selectN = new int[6];
		Random rand = new Random(3);
		System.out.println("선택번호: ");
		for(int i=0;i<selectN.length; i++) {
			selectN[i] = rand.nextInt(45)+1;
			System.out.print(selectN[i]+" ");
		}
		System.out.println();
		
		int[] winN = new int[6];
		rand = new Random(5);
		System.out.println("당첨번호: ");
		for(int i=0;i<winN.length; i++) {
			winN[i] = rand.nextInt(45)+1;
			System.out.print(winN[i]+" ");
		}
		System.out.println();
		
		Arrays.sort(selectN);
		Arrays.sort(winN);
		boolean result = Arrays.equals(selectN, winN);
		System.out.println("당첨여부: ");
		if(result) {
			System.out.println("1등에 당첨되셨습니다.");
		} else {
			System.out.println("당첨되지 않았습니다.");
		}
	}

}
