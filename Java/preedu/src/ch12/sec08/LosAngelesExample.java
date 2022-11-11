package ch12.sec08;

import java.util.Calendar;
import java.util.TimeZone;

public class LosAngelesExample {

	public static void main(String[] args) {
		TimeZone tZ = TimeZone.getTimeZone("America/Los_Angeles");
		Calendar now = Calendar.getInstance(tZ);
		
		int amPm = now.get(Calendar.AM_PM);
		String straPm = null;
		if(amPm == Calendar.AM) {
			straPm = "오전";
		} else {
			straPm = "오후";
		}
		

		int hour = now.get(Calendar.HOUR);
		int minute = now.get(Calendar.MINUTE);
		int second = now.get(Calendar.SECOND);
		
		System.out.print(straPm + " ");
		System.out.print(hour + "시 ");
		System.out.print(minute + "분 ");
		System.out.println(second + "초 ");

		
		TimeZone tZ2 = TimeZone.getTimeZone("Europe/London");
		Calendar now2 = Calendar.getInstance(tZ2);
		
		int amPm2 = now2.get(Calendar.AM_PM);
		String straPm2 = null;
		if(amPm2 == Calendar.AM) {
			straPm2 = "오전";
		} else {
			straPm2 = "오후";
		}
		

		int hour2 = now2.get(Calendar.HOUR);
		int minute2 = now2.get(Calendar.MINUTE);
		int second2 = now2.get(Calendar.SECOND);
		
		System.out.print(straPm2 + " ");
		System.out.print(hour2 + "시 ");
		System.out.print(minute2 + "분 ");
		System.out.println(second2 + "초 ");
		
		
		TimeZone tZ3 = TimeZone.getTimeZone("Asia/Seoul");
		Calendar now3 = Calendar.getInstance(tZ3);
		
		int amPm3 = now3.get(Calendar.AM_PM);
		String straPm3 = null;
		if(amPm3 == Calendar.AM) {
			straPm3 = "오전";
		} else {
			straPm3 = "오후";
		}
		

		int hour3 = now3.get(Calendar.HOUR);
		int minute3 = now3.get(Calendar.MINUTE);
		int second3 = now3.get(Calendar.SECOND);
		
		System.out.print(straPm3 + " ");
		System.out.print(hour3 + "시 ");
		System.out.print(minute3 + "분 ");
		System.out.println(second3 + "초 ");
		
		
		TimeZone tZ4 = TimeZone.getTimeZone("America/New_York");
		Calendar now4 = Calendar.getInstance(tZ4);
		
		int amPm4 = now4.get(Calendar.AM_PM);
		String straPm4 = null;
		if(amPm4 == Calendar.AM) {
			straPm4 = "오전";
		} else {
			straPm4 = "오후";
		}
		

		int hour4 = now4.get(Calendar.HOUR);
		int minute4 = now4.get(Calendar.MINUTE);
		int second4 = now4.get(Calendar.SECOND);
		
		System.out.print(straPm4 + " ");
		System.out.print(hour4 + "시 ");
		System.out.print(minute4 + "분 ");
		System.out.println(second4 + "초 ");
	}
}
