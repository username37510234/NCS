package ch12.sec12;

import java.lang.reflect.Method;

public class PrintAnnotationExample {

	public static void main(String[] args) throws Exception{

		Method[] declaredMethods = Service.class.getDeclaredMethods();
		for(Method method : declaredMethods) {
			PrintAnnotation pA = method.getAnnotation(PrintAnnotation.class);
			
			printLine(pA);
			
			method.invoke(new Service());
			
			printLine(pA);
		}
	}
	
	public static void printLine(PrintAnnotation pA) {
		if(pA != null) {
			int number = pA.number();
			for(int i=0;i<number; i++) {
				String value = pA.value();
				System.out.print(value);
			}
			System.out.println();
		}
	}

}
