package ch05.sec05;

public class EqualsExample {

	public static void main(String[] args) {
		String strvar1 = "홍길동";
		String strvar2 = "홍길동";
		
		if(strvar1 == strvar2) {
			System.out.println("strvar1과 strvar2는 참조가 같음");
		} else {
			System.out.println("strvar1과 strvar2는 참조가 다름");
		}
		
		if(strvar1.equals(strvar2)) {
			System.out.println("strvar1과 strvar2는 문자열이 같음");
		}

		String strvar3 = new String("홍길동");
		String strvar4 = new String("");
		
		if(strvar3 == strvar4) {
			System.out.println("strvar3과 strvar4는 참조가 같음");
		} else {
			System.out.println("strvar3과 strvar4는 참조가 다름");
		}
		
		if(strvar3.equals(strvar4)) {
			System.out.println("strvar3과 strvar4는 문자열이 같음");
		} else {
			System.out.println("strvar3과 strvar4는 다른 문자열입니다.");
		}
	}

}
