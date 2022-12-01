package ch12.sec08;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class DateTimeCompareExample {

	public static void main(String[] args) {
		
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy.MM.dd a HH:mm:ss");
		
		LocalDateTime sdt = LocalDateTime.of(2022, 1, 1, 0, 0, 0);
		System.out.println("시작일: "+sdt.format(dtf));
		
		LocalDateTime edt = LocalDateTime.of(2022, 12, 31, 0, 0, 0);
		System.out.println("종료일: "+edt.format(dtf));
		
		if(sdt.isBefore(edt)) {
			System.out.println("진행중입니다.");
		} else if(sdt.isEqual(edt)) {
			System.out.println("종료합니다.");
		} else if(sdt.isAfter(edt)) {
			System.out.println("종료했습니다.");
		}
		
		long rY = sdt.until(edt, ChronoUnit.YEARS);
		long rM = sdt.until(edt, ChronoUnit.MONTHS);
		long rD = sdt.until(edt, ChronoUnit.DAYS);
		long rH = sdt.until(edt, ChronoUnit.HOURS);
		long rm = sdt.until(edt, ChronoUnit.MINUTES);
		long rS = sdt.until(edt, ChronoUnit.SECONDS);
		System.out.println("남은 해: " +rY);
		System.out.println("남은 월: " +rM);
		System.out.println("남은 일: " +rD);
		System.out.println("남은 시: " +rH);
		System.out.println("남은 분: " +rm);
		System.out.println("남은 초: " +rS);
		
	}

}
