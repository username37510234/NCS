package ch12.sec08;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class DateTimeCompareExample {

	public static void main(String[] args) {
		
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy.MM.dd a HH:mm:ss");
		
		LocalDateTime sDT = LocalDateTime.of(2021, 1, 1, 0, 0, 0);
		System.out.println("시작일: "+sDT.format(dtf));
		LocalDateTime eDT = LocalDateTime.of(2023, 12, 31, 0, 0);
		System.out.println("종료일: "+eDT.format(dtf));
		
		if(sDT.isBefore(eDT)) {
			System.out.println("진행중입니다.");
		} else if(sDT.isEqual(eDT)) {
			System.out.println("종료합니다.");
		} else if(sDT.isAfter(eDT)) {
			System.out.println("종료했습니다.");
		}
		
		long remainY = sDT.until(eDT, ChronoUnit.YEARS);
		long remainM = sDT.until(eDT, ChronoUnit.MONTHS);
		long remainD = sDT.until(eDT, ChronoUnit.DAYS);
		long remainH = sDT.until(eDT, ChronoUnit.HOURS);
		long remainMi = sDT.until(eDT, ChronoUnit.MINUTES);
		long remainS = sDT.until(eDT, ChronoUnit.SECONDS);
		
		System.out.println("남은 해: " + remainY +"년");
		System.out.println("남은 달: " + remainM +"월");
		System.out.println("남은 일: " + remainD +"일");
		System.out.println("남은 시간: " + remainH +"시간");
		System.out.println("남은 분: " + remainMi +"분");
		System.out.println("남은 초: " + remainS +"초");
	}

}
