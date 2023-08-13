import java.util.*;

public class Main {
    public String solution(String a) {
        int m = Integer.MIN_VALUE, pos;
        String answer = "";
        pos = a.indexOf(",");
        while(-1 != pos){
            String temp = a.substring(0,pos);
            pos = a.indexOf(",");
            int len = temp.length();
            if(len > m){
                m = len;
                answer = temp;
            }
            a = a.substring(pos+1);
        }
        if (a.length() > m) {
            return a;
        } else {
            return answer;
        }
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String a = kb.next();
        System.out.println(T.solution(a));
    }
}