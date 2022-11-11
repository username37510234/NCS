package ch12.sec03.exam02;

import java.util.HashSet;

public class HashSetExample {

	public static void main(String[] args) {
		HashSet HSt = new HashSet();
		
		Student s1 = new Student(1, "홍길동");
		HSt.add(s1);
		System.out.println("저장된 객체수: " + HSt.size());
		Student s2 = new Student(1, "홍길동");
		HSt.add(s2);
		System.out.println("저장된 객체수: " + HSt.size());
		Student s3 = new Student(2, "홍길동");
		HSt.add(s3);
		System.out.println("저장된 객체수: " + HSt.size());
		Student s4 = new Student(2, "황길동");
		HSt.add(s4);
		System.out.println("저장된 객체수: " + HSt.size());
	}

}
