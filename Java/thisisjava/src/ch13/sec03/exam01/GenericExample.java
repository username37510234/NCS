package ch13.sec03.exam01;

public class GenericExample {

	public static <T> Box<T> boxing(T t){

		Box<T> box = new Box<T>();
		box.set(t);
		return box;
	}
	public static void main(String[] args) {
		
		Box<Integer> b1 = boxing(100);
		int intV = b1.get();
		System.out.println(intV);
		
		Box<String> b2 = boxing("홍길동");
		String strV = b2.get();
		System.out.println(strV);
		
	}

}
