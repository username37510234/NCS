package ch07.sec04.exam01;

public class ComputerExample {

	public static void main(String[] args) {
		int r = 10;
		
		Calculator calC = new Calculator();
		System.out.println("원 면적: "+calC.areaCircle(r));
		System.out.println();
		
		Computer comp = new Computer();
		System.out.println("원 면적: "+comp.areaCircle(r));
		System.out.println();
	}

}
