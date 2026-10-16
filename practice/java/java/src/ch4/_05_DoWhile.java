package ch4;

public class _05_DoWhile {
    public static void main(String[] agrs){
        int distance = 25;
        int move = 0;
        int height = 25;

        do {
            System.out.println("진행중");
            System.out.println("이동거리 " + move);

        } while (move + height > distance); {
            System.out.println("이동완료");
        }
    }
}
