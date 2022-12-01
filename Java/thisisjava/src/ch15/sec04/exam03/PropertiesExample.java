package ch15.sec04.exam03;

import java.util.Properties;

public class PropertiesExample {

    public static void main(String[] args) throws Exception {
        
        Properties proper = new Properties();
        
        proper.load(PropertiesExample.class.getResourceAsStream("database.properties"));
        
        String driver = proper.getProperty("driver");
        String url = proper.getProperty("url");
        String username = proper.getProperty("username");
        String password = proper.getProperty("password");
        String admin = proper.getProperty("admin");
        
        System.out.println("driver : "+driver);
        System.out.println("url : "+url);
        System.out.println("username : "+username);
        System.out.println("password : "+password);
        System.out.println("admin : "+admin);
    }

}
