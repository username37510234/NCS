package ch12.sec08;

import java.util.TimeZone;

public class PrintTimeZoneID {

	public static void main(String[] args) {
		String[] IDs = TimeZone.getAvailableIDs();
		for(String id : IDs) {
			System.out.println(id);
		}
	}

}
