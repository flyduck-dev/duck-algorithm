import java.util.Locale;
import java.util.Scanner;

public class Main {
    public int solution(String a, char b) {
        int answer = 0;
        a = a.toUpperCase();
        b = Character.toUpperCase(b);
        for (char i : a.toCharArray()){
            if (i==b){
                answer++;
            }
        }
//        for (int i=0; i<a.length(); i++){
//            if(a.charAt(i) == b){
//                answer++;
//            }
//        }
        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String a = kb.next();
        char b = kb.next().charAt(0);
        System.out.println(T.solution(a,b));
        for (int i = 1; i <= 5; i++) {
            System.out.println("i = " + i);
        }
    }
}
