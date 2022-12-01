package ch12.sec08;

import java.util.Calendar;

public class CalendarExample {

	public static void main(String[] args) {
		
		Calendar now = Calendar.getInstance();
		
		int year = now.get(Calendar.YEAR);
		int mo = now.get(Calendar.MONTH);
		int day = now.get(Calendar.DAY_OF_MONTH);
		int week = now.get(Calendar.DAY_OF_WEEK);
		String strW = null;
		switch(week) {
		case Calendar.MONDAY: strW = "월요일";break;
		case Calendar.TUESDAY: strW = "화요일";break;
		case Calendar.WEDNESDAY: strW = "수요일";break;
		case Calendar.THURSDAY: strW = "목요일";break;
		case Calendar.FRIDAY: strW = "금요일";break;
		case Calendar.SATURDAY: strW = "토요일";break;
		case Calendar.SUNDAY: strW = "일요일";break;
		}
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
		
		System.out.println(year+"년 "+mo+"월 "+day+"일 ");
		System.out.println(strW+"요일 "+strampm+" ");
		System.out.println(hour+"시 "+min+"분 "+sec+"초 ");
	}

}
