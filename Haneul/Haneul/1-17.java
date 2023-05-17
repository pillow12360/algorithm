package Haneul;

class Solution_17 {
    public String solution(int n) {
         String answer = "";
         for(int i = 1; i <= n; i++) {
             if(n > 10000) { // 10000이상이면 예외 발생 
                 System.out.println("n은 길이 10,000이하인 자연수입니다.");
                 break;
             }
             if(i%2 == 1) { // i가 홀수일땐 "수", 짝수일땐 "박"
                 answer += "수";
             } else {
                 answer += "박";
             }
         }
         return answer;
     }
 }