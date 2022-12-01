package ch15.sec99;

public class Student11 implements Comparable<Student11>{
    public String id;
    public int score;
    public Student11(String id, int score) {
        this.id = id;
        this.score = score;
    }
    @Override
    public int compareTo(Student11 o) {
        if(score>o.score) return 1;
        else if(score==o.score) return 0;
        else return -1;
    }
}
