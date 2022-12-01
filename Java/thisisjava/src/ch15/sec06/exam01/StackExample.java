package ch15.sec06.exam01;

import java.util.Stack;

public class StackExample {

    public static void main(String[] args) {

        Stack<Coin> coinB = new Stack<Coin>();

        coinB.add(new Coin(100));
        coinB.add(new Coin(50));
        coinB.add(new Coin(500));
        coinB.add(new Coin(10));

        while(!coinB.isEmpty()) {
            Coin coin = coinB.pop();
            System.out.println("꺼내온 동전 : " + coin.getValue()+"원");
        }
    }
}
