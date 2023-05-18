package Haneul;

class Solution_10 {
    public long solution(int a, int b) {
         long result = 0;
          int max = 0;
         int min = 0;
         if(a > b) {
             max = a;
             min = b;
         } else if(a < b){
             min = a;
             max = b;
         }
         for(int i = min; i <= max; i++) {
             if(a == b) {
             return a;
         }
             result += i; //     5
         }
         return result;
  }
}


