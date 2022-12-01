package ch15.sec02.exam03;

import java.util.ArrayList;
import java.util.List;

public class LinkedListExample {

    public static void main(String[] args) {
        
        List<String> list1 = new ArrayList<String>();
        
        List<String> list2 = new ArrayList<String>();
        
        long startT;
        long endT;
        
        startT = System.nanoTime();
        for(int i=0; i<10000; i++) {
            list1.add(0, String.valueOf(i));
        }
        endT = System.nanoTime();
        System.out.printf("%-17s %8d ns \n", "ArrayList 걸린 시간: ", (endT-startT));
        
        startT = System.nanoTime();
        for(int i=0; i<10000; i++) {
            list2.add(0, String.valueOf(i));
        }
        endT = System.nanoTime();
        System.out.printf("%-17s %8d ns \n", "LinkedList 걸린 시간", (endT-startT));
    }

}
