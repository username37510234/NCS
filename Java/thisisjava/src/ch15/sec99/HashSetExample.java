package ch15.sec99;

import java.util.HashSet;
import java.util.Set;

public class HashSetExample {

    public static void main(String[] args) {

        Set<Student22> set = new HashSet<Student22>();

        set.add(new Student22(1, "홍길동"));
        set.add(new Student22(2, "신용권"));
        set.add(new Student22(1, "조민우"));

        System.out.println("저장된 객체수: "+set.size());
        for(Student22 s : set) {
            System.out.println(s.studentNum + ":" +s.name);
        }
    }
}
