package ch3;

public class _04_EscapeSequence{
    public static void main(String[] args) {
        // 특수문자, 이스케이프 문자
        int a = 5;
        int b = 6;
        System.out.println("오늘\n기분이\n좋다"); //    \n: 줄 바꿈
        System.out.println("김밥\t3000원"); //     \t: 탭
        System.out.println("ㄴㅇㄴㅇ\\"); //      \\: \
        System.out.println("내 이름은\"000\" "); //     \": "
        System.out.printf("a = %d %nb = %d%n", a, b);  // %d 정수 %f 실수 %n 줄 바꿈 %s 문자열
    }
}
