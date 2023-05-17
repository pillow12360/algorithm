package Haneul;

class Solution_2 {
    public double solution(int[] arr) {
        double answer = 0;
        double result = 0;
        for(int i =0; i< arr.length; i++){
            result += arr[i];
            answer = result / arr.length;
        }
        return answer;
    }
} 
