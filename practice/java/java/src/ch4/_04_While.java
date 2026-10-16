package ch4;

public class _04_While {
    public static void main(String[] agrs) {
        int distance = 30;
        int move = 0;
        while (move < distance) {
            System.out.println("진행중" + move);
            move += 3;
        }
        System.out.println("도착");
    }
}
