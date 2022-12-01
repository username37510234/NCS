package ch15.sec99;

import java.util.TreeSet;

public class TreeSetExample {
    public static void main(String[] args) {
        TreeSet<Student11> treeSet = new TreeSet<Student11>();
        treeSet.add(new Student11("blue",96));
        treeSet.add(new Student11("hong",86));
        treeSet.add(new Student11("white",92));

        Student11 student = treeSet.last();
        System.out.println("최고 점수: "+ student.score);
        System.out.println("최고 점수를 받은 아이디: "+student.id);
    }
}
