package ch06.sec99;

public class Member {

	public static void main(String[] args) {
		MemberService memSer = new MemberService();
		boolean result = memSer.login("hong", "12345");
		if (result) {
			System.out.println("로그인 되었습니다.");
			memSer.logout("hong");
		} else {
			System.out.println("id 또는 password가 올바르지 않습니다.");
		}
	}

}
