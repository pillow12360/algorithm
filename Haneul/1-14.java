package Haneul;
class Solution_14 {
    public String solution(String phone_number) {
        char[] a = phone_number.toCharArray();
       for(int i = 0; i < a.length-4; i++) {
            a[i] = '*';
       }
    String st = new String(a);
    return st;
        } 
    
    }