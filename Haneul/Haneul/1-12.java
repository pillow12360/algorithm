package Haneul;
import java.util.ArrayList;
import java.util.Arrays;

class Solution_12 {
    public String solution(String[] seoul) {
      	ArrayList<String> array = new ArrayList(Arrays.asList(seoul)); 
	    return "김서방은 " + array.indexOf("Kim") + "에 있다";   
    }
}