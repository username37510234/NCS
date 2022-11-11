
public class Student {

	private String name;
	private int kor;
	private int eng;
	private int total;
	
	Student(String name, int kor, int eng){
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		
		this.total = kor+eng;
	}

	public String getName() {
		return name;
	}

	public int getTotal() {
		return total;
	}
	
}
