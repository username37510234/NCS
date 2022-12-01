package ch15.sec06.exam02;

import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {

    public static void main(String[] args) {

        Queue<Message> mQu = new LinkedList<>();

        mQu.offer(new Message("sendMail", "홍길동"));
        mQu.offer(new Message("sendSMS", "신용권"));
        mQu.offer(new Message("sendKakaotalk", "감자바"));

        while(!mQu.isEmpty()) {
            Message message = mQu.poll();
            switch(message.command) {
                case "sendMail":
                    System.out.println(message.to+"님에게 메일을 보냅니다.");
                    break;
                case "sendSMS":
                    System.out.println(message.to+"님에게 SMS를 보냅니다.");
                    break;
                case "sendKakaotalk":
                    System.out.println(message.to+"님에게 카카오톡을 보냅니다.");
                    break;
            }
        }
    }

}
