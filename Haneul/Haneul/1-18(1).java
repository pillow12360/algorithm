package Haneul;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution_18 {
    public String solution1(String s) {
       String[] str = s.split("");
       List<String> list = new ArrayList<>(Arrays.asList(str));    
       
       Collections.sort(list, Collections.reverseOrder());
       String answer = list.toString();
       return answer;
        
    }
}
