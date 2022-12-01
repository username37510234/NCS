package ch15.sec99;

public class Student22 {

    public int studentNum;
    public String name;
    public Student22(int studentNum, String name) {
        this.studentNum = studentNum;
        this.name = name;
    }
    @Override
    public int hashCode() {
        // TODO Auto-generated method stub
        return studentNum;
    }
    @Override
    public boolean equals(Object obj) {
        if(obj instanceof Student22 target) {
            return target.studentNum==studentNum;
        }else {
            return false;
        }
    }
}
