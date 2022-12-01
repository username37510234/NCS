package ch15.sec99;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class MapExample {

    public static void main(String[] args) {

        Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("blue", 96);
        map.put("hong", 86);
        map.put("white", 92);

        String name = null;
        int maxScore = 0;
        int totalScore = 0;

        Set<Map.Entry<String, Integer>> lol = map.entrySet();
        for(Map.Entry<String, Integer> ll : lol) {
            if(ll.getValue() > maxScore) {
                name = ll.getKey();
                maxScore = ll.getValue();
            }
            totalScore += ll.getValue();
        }
        System.out.println("최고 점수를 받은 아이디 : "+name);
        System.out.println("최고 점수 : "+maxScore);
        System.out.println("평균 점수 : "+totalScore/map.size());
    }
}
