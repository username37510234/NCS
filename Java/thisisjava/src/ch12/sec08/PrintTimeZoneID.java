package ch12.sec08;

import java.util.TimeZone;

public class PrintTimeZoneID {

	public static void main(String[] args) {
		
		String[] availIDs = TimeZone.getAvailableIDs();
		for(String id : availIDs) {
			System.out.println(id);
		}
	}

}
