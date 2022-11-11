package ch12.sec08;

import java.util.Calendar;

public class CalendarExample {

	public static void main(String[] args) {
		
		Calendar now = Calendar.getInstance();
		
		int year = now.get(Calendar.YEAR);
		int month = now.get(Calendar.MONTH);
		int day = now.get(Calendar.DAY_OF_MONTH);
		int week = now.get(Calendar.DAY_OF_WEEK);
		String strW = null;
		switch(week) {
		case Calendar.MONDAY: strW = "월";break;
		case Calendar.TUESDAY: strW = "화";break;
		case Calendar.WEDNESDAY: strW = "수";break;
		case Calendar.THURSDAY: strW = "목";break;
		case Calendar.FRIDAY: strW = "금";break;
		case Calendar.SATURDAY: strW = "토";break;
		case Calendar.SUNDAY: strW = "일";break;
		default: System.out.println("오류");
		}
		
		int aPm = now.get(Calendar.AM_PM);
		String straPm = null;
		if(aPm == Calendar.AM) {
			straPm = "오전";
		} else {
			straPm = "오후";
		}
		
		int hour = now.get(Calendar.HOUR);
		int minute = now.get(Calendar.MINUTE);
		int second = now.get(Calendar.SECOND);
		
		System.out.print(year + "년 ");
		System.out.print(month + "월 ");
		System.out.println(day + "일 ");
		System.out.print(strW + "요일 ");
		System.out.println(straPm + " ");
		System.out.print(hour + "시 ");
		System.out.print(minute + "분 ");
		System.out.print(second + "초 ");
	}

}
