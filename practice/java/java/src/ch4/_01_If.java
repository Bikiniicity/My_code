package ch4;

public class _01_If {
    public static void main(String[] args) {
        int hour = 8;
        if (hour < 10 || hour == 9){ // ||: or &&: and
            System.out.println("To late");
        } else if(hour == 8) {
            System.out.println("good");
        }
    }
}
