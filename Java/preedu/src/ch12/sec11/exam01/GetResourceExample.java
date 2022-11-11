package ch12.sec11.exam01;

public class GetResourceExample {

	public static void main(String[] args) {
		Class clazz = Car.class;
		
		String p1P = clazz.getResource("photo1.jpg").getPath();
		String p2P = clazz.getResource("images/photo2.jpg").getPath();
		
		System.out.println(p1P);
		System.out.println(p2P);
	}

}
