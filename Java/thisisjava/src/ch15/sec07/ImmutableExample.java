package ch15.sec07;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class ImmutableExample {

    public static void main(String[] args) {
        
        List<String> immutList1 = List.of("A","B","C");
        
        Set<String> immutSet1 = Set.of("A","B","C");
        
        Map<Integer, String> immutMap1 = Map.of(
                1, "A",
                2, "B",
                3, "C"                
                );
        
        List<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");
        list.add("C");
        List<String> immutList2 = List.copyOf(list);
        
        Set<String> set = new HashSet<>();
        set.add("A");
        set.add("B");
        set.add("C");
        Set<String> immutSet2 = Set.copyOf(set);
        
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "A");
        map.put(2, "B");
        map.put(3, "C");
        Map<Integer, String> immutMap2 = Map.copyOf(map);
        
        String[] arr = { "A","B","C","D"};
        List<String> immutList3 = Arrays.asList(arr);
        
        for(int i=0; i<immutList1.size(); i++) {
            String p = immutList1.get(i);
            System.out.print(p);
        }
        System.out.println();
        
        for(int i=0; i<immutList2.size(); i++) {
            String p = immutList2.get(i);
            System.out.print(p);
        }
        System.out.println();
        
        for(int i=0; i<immutList3.size(); i++) {
            String p = immutList3.get(i);
            System.out.print(p);
        }
        System.out.println();
        
        for(int i=1; i<=immutMap1.size(); i++) {
            String p = immutMap1.get(i);
            System.out.print(p);
        }
        System.out.println();
        
        for(int i=1; i<=immutMap2.size(); i++) {
            String p = immutMap2.get(i);
            System.out.print(p);
        }
        System.out.println();
        
        for(String s : immutSet1) {
            System.out.print(s);
        }
        System.out.println();
        
        for(String s : immutSet2) {
            System.out.print(s);
        }
        System.out.println();
        
        
    }

}
