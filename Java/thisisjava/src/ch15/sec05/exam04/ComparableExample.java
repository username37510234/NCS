package ch15.sec05.exam04;

import java.util.TreeSet;

public class ComparableExample {

    public static void main(String[] args) {

        TreeSet<Fruit> tSt = new TreeSet<Fruit>(new FruitComparator());

        tSt.add(new Fruit("포도",3000));
        tSt.add(new Fruit("수박",10000));
        tSt.add(new Fruit("딸기",6000));

        for(Fruit fruit : tSt) {
            System.out.println(fruit.name+": "+fruit.price+"원");
        }
    }
}
