package ch1;

public class _ch7_Typecasting {
    public static void main(String[] args) {
        int a = 20;
        double b = 20.1;
        System.out.println((int) b);

        int sum = 98 + (int) 10.2;
        System.out.println(sum);

        //숫자를 문자열로
        String s1 = String.valueOf(93);
        s1 = Integer.toString(93);
        System.out.println(s1);

        //문자를 숫자열로
        int i = Integer.parseInt("93");
        System.out.println(i);
    }
}
