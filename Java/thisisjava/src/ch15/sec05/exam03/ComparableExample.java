package ch15.sec05.exam03;

import java.util.TreeSet;

public class ComparableExample {

    public static void main(String[] args) {

        TreeSet<Person> tSt = new TreeSet<Person>();

        tSt.add(new Person("홍길동",45));
        tSt.add(new Person("감자바",25));
        tSt.add(new Person("박지원",31));

        for(Person person : tSt) {
            System.out.println(person.name + ": "+person.age);
        }
    }
}