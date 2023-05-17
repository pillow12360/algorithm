package Haneul;

import java.util.Arrays;
import java.util.Collections;


class Solution_18 {
 	 public String solution(String s) {
		 String answer = "";
		 String[] str = s.split("");
	 
		 Arrays.sort(str, Collections.reverseOrder());

	       for(String result : str) {
	    	   answer += result;
	       }
	       return answer;
	        
	    }
}