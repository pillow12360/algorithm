package Haneul;

import java.util.ArrayList;
class Solution_15 {
public int[] solution(int[] arr) {
		  ArrayList<Integer> an = new ArrayList<>();
	    	int[] a = new int[]{-1};
	    	int min = arr[0];
	    	for(int i = 1; i < arr.length; i++) {
	    		min = Math.min(min, arr[i]);
	    	}
	    	for(int i = 0; i < arr.length; i++) {
	    		if(min != arr[i]) {
	    			an.add(arr[i]);
	    		}
	    	}
	    		int[] result = new int[an.size()];
	    		for(int i = 0; i < an.size(); i++) {
	    			result[i] = an.get(i);
	    	}
	    		if(result.length == 0) {
	    	    	   return a;
	    	       }
	    		return result;
	}
}
