
public class MyReport {
	public static void main(String[] args) {

		String name = "홍길동";
		String teleph_no = "01012345678";
		String city = "서울";
		String area = "노원";
		
		System.out.println("이름 : "+name);
		System.out.println("전화번호 : "+teleph_no);
		System.out.printf("사는 곳 : %s시 %s구",city,area);
	}
}
