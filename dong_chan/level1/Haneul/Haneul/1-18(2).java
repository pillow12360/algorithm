package Haneul;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution_18 {
	 public String solution(String s) {
		 String answer = "";
	       String[] str = s.split("");
	       List<String> list = new ArrayList<>(Arrays.asList(str));    
	       
	       Collections.sort(list, Collections.reverseOrder());
	       for(String result : list) {
	    	   answer += result;
	       }
	       return answer;
	        
	    }
}
