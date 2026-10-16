package ch4;
// 1등:전액장학금 | 2,3등:반액장학금 | 4등~: 장학금 대상아님
public class _02_SwitchCase {
    public static void main(String[] args){
        int ranking = 2;

        switch (ranking) {
            case 1:
                System.out.println("전액장학금");
                break;
            case 2:
            case 3:
                System.out.println("반액장학금");
                break;
            case 4:
                System.out.println("장학금 대상 아님");
                break;
            default:
                System.out.println("장학금");

        }
        System.out.println("장학금 조회");
    }
}
