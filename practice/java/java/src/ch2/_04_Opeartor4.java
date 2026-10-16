package ch2;

public class _04_Opeartor4 {
    public static void main(String[] args) {
        //System.out.println("A" || "B"); // or연산자
        //System.out.println("A" && "B"); // and연산자


        // 삼항 연산자
        int x = 5;
        int y = 3;
        // 결과 = (조건) ? (참인경우):(거짓인 경우)
        int max = (x > y) ? x:y;
        System.out.println(max);
    }
}
