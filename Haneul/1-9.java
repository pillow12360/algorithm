package Haneul;

class Solution_9 {
    public boolean solution(int x) {
                long answers = 0;
                boolean answer = true;  
                String a = Integer.toString(x);
                char[] ch = a.toCharArray();
                for(int i = 0; i < ch.length; i++) {
                    answers += Character.getNumericValue(ch[i]);
                }
                if(x%answers == 0) {
                    return answer;
                } else {
                    return false;
                }
             
            }
    }