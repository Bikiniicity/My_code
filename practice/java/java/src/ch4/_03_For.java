package ch4;

public class _03_For {
    public static void main(String[] args) {
        // for(선언; 조건; 증감;){
        //  수행명령
        for (int i = 0; i < 10; i++) {
            System.out.println("어서오세요. 냥냥입니다." + i);

        }
        for (int i = 0; i < 10 ; i+= 2) {
            System.out.println(i);
            //System.out.print(i); // 줄바꿈 안 함 print()
        }
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
        }
        System.out.println(sum);
    }
}
