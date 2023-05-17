package Haneul;

import java.util.ArrayList;
import java.util.Collections;
class Solution_13 {
	int stack = 0;
	int[] ab = {-1};
	ArrayList<Integer> a = new ArrayList<>();
public int[] solution(int[] arr, int divisor) {
	
	for(int i = 0; i < arr.length; i++) {
	if(arr[i]%divisor == 0) {
		a.add(arr[i]);
	} else if(arr[i]%divisor != 0) {
		stack++;
	}
	if(stack == arr.length) {
		return ab;
	}
	}
	Collections.sort(a);
	int[] result = new int[a.size()];
	for(int i =0; i < a.size(); i++) {
	result[i] = a.get(i);
	}
	return result;
	
}
}
