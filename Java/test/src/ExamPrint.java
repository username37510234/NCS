
public class ExamPrint {

	public static void main(String[] args) {

		Student[] arrstudent = new Student[4];

		arrstudent[0] = new Student("홍길동",60,75);
		arrstudent[1] = new Student("강호동",70,80);
		arrstudent[2] = new Student("유재석",80,55);
		arrstudent[3] = new Student("박명수",90,100);

		for(int i=0; i<arrstudent.length; i++) {
			for(int j=0; j<arrstudent.length; j++) {
				if(arrstudent[i].getTotal() > arrstudent[j].getTotal()) {
					Student tmp = arrstudent[j];
					arrstudent[j] = arrstudent[i];
					arrstudent[i] = tmp;
				}
			}
		}
		int ord = 1;
		for(int i=0; i<arrstudent.length; i++) {
			System.out.printf("이름: %s\t 총점: %s\t 순위: %d\n",arrstudent[i].getName(),arrstudent[i].getTotal(),ord);
			if(i<arrstudent.length - 1 && arrstudent[i].getTotal()!=arrstudent[i+1].getTotal()) {ord++;}
		}
	}
}
