package Haneul;
import java.util.Arrays;
class Solution_8 {
        public long solution(long n) {
      String a = Long.toString(n);
      char[] array = a.toCharArray();
      Arrays.sort(array);
      String st = new String(array);
      st = new StringBuilder(st).reverse().toString();
      Long answer = Long.parseLong(st);
      return answer;
    }
}
