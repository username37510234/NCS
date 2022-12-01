package ch12.sec08;

import java.util.Calendar;
import java.util.TimeZone;

public class LosAngelesExample {

	public static void main(String[] args) {
		
		TimeZone tz = TimeZone.getTimeZone("America/Los_Angeles");
		Calendar now = Calendar.getInstance(tz);
		
		int ampm = now.get(Calendar.AM_PM);
		String strampm = null;
		if(ampm == Calendar.AM) {
			strampm = "오전";
		} else {
			strampm = "오후";
		}
		int hour = now.get(Calendar.HOUR);
		int min = now.get(Calendar.MINUTE);
		int sec = now.get(Calendar.SECOND);
		
		System.out.println(strampm+" "+hour+"시 "+min+"분 "+sec+"초 ");
	}

}
