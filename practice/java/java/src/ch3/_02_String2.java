package ch3;

public class _02_String2 {
    public static void main(String[] args) {
        String s = "I Like Java.";

        System.out.println(s.replace("Java", "Python")); // 대체 출력
        System.out.println(s.substring(3)); // index (n)번 부터 출력

        // 지정한 부분 ~ 지정부분 -1까지
        System.out.println(s.substring(s.indexOf("Like"),s.indexOf(".")));

        s = "            Like Java        ";
        System.out.println(s.trim()); // 띄어쓰기 제거

        // 문자 결합
        String s1 = "java";
        String s2 = "python";

        System.out.println(s1+s2);
        System.out.println(s1 + " ," + s2);
        System.out.println(s1.concat(" ,").concat(s2));
    }
} 
