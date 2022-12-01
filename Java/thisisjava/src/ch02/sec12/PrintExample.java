package ch02.sec12;

public class PrintExample {

	public static void main(String[] args) {
		int value = 123;
		System.out.printf("상품의 가격%d원\n", value);
		System.out.printf("상품의 가격%6d원\n", value);
		System.out.printf("상품의 가격%-6d원\n", value);
		System.out.printf("상품의 가격%06d원\n", value);
		
		int a = 10;
		double area = 3.14159 * a * a;
		System.out.printf("반지름이 %d인 원의 넓이:%10.2f\n", 10, area);
		
		int index=1;
		String name = "홍길동";
		String job = "도적";
		System.out.printf("%1$06d|%2$-6s|%3$6s\n",index++,name,job);
		System.out.printf("%1$06d|%2$-6s|%3$6s\n",index++,"홍망령","전사");
		System.out.printf("%1$06d|%2$-6s|%3$6s\n",index++,"홍장미","마법사");
		System.out.printf("%1$06d|%2$-6s|%3$6s\n",index++,name,job);
		System.out.printf("%1$06d|%2$-6s|%3$6s\n",index++,name,job);
	}

}
