package ch3;

public class _03_StringCompare {
    public static void main(String[] args) {
        // 문자열 비교
        String s1 = "Java";
        String s2 = "Python";

        System.out.println(s1.equals(s2));
        System.out.println(s1.equals("Java")); // 내용 비교
        System.out.println(s1 == s2); // 참조 비교

        // 대소문자 상관없이 문자열이 같은지 비교
        System.out.println(s1.equalsIgnoreCase("java "));

    }
}
