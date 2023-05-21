package Haneul;

class Solution_5 {
    public long[] solution(long n) {
            String st = String.valueOf(n);
            char[] c = st.toCharArray();
            long[] answer = new long[c.length];
            for(int i = st.length()-1; i >= 0; i--) { 
                answer[st.length()-1-i] = st.charAt(i)-'0'; 
                }
            return answer;
        }
        }
