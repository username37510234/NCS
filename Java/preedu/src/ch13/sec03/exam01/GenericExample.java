package ch13.sec03.exam01;

public class GenericExample {
	
	public static <T> Box<T> Boxing(T t){
		Box<T> box = new Box<T>();
		box.set(t);
		return box;
	}

	public static void main(String[] args) {

		Box<Integer> box1 = Boxing(100);
		int intValue = box1.get();
		System.out.println(intValue);
		
		Box<String> box2 = Boxing("홍길동");
		String strValue = box2.get();
		System.out.println(strValue);
	}

}
