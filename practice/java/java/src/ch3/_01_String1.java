package ch3;

import java.util.Locale;

public class _01_String1 {
    public static void main(String[] args) {
        String s = "I love java";
        System.out.println(s);

        System.out.println(s.length()); //11

        System.out.println(s.toUpperCase()); // 대문자
        System.out.println(s.toLowerCase()); // 소문자
        System.out.println(s.equals("I love jav")); // equals인지
        System.out.println(s.contains("java")); //확인 여부
        System.out.println(s.indexOf("java")); //인덱스값 반환
        System.out.println(s.lastIndexOf("java")); //뒤에서 부터 인덱스 값 반환
        System.out.println(s.startsWith("I")); // N으로 시작하는가
        System.out.println(s.endsWith("e")); // N으로 끝나는가
    }
}
