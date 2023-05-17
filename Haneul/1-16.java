package Haneul;

class Solution_16 {
    public String solution(String s) {
                int startIndex = s.length()/2-1;
                int endIndex = startIndex+1;
                if(s.length()%2 == 0) {
                    return s.substring(startIndex, endIndex+1);
                } else {
                    return String.valueOf(s.charAt(endIndex));
                }
            }
    }