package teste;

import java.util.Arrays;

public class MergeSortMain {
	
	public static void main(String[] args) {
		MergeSort<Integer> mg = new MergeSort<Integer>();
		Integer[] array = {3,2,1,5}; 
		mg.sort(array, 0, array.length-1);
		
		System.out.println(Arrays.asList(array));
	}
}
