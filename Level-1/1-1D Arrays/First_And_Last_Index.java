import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    
    Scanner input = new Scanner(System.in);
    int size = input.nextInt();
    int[] arr = new int[size];
    
    for (int i = 0; i < size; i++) {
        arr[i] = input.nextInt();
    }
    
    int target = input.nextInt();

    FirstAndLast(arr, target);
 }

public static void FirstAndLast(int[] arr, int target) {

	//Time Complexity: O(log n)
	//Based on Binary Search

	//Find first index by changing the end point when element == target
	int start = 0;
	int end = arr.length - 1;
	int first = -1;

	while (start <= end) {
		int mid = (start + end) / 2;

		if (arr[mid] > target) {
			end = mid - 1;
		} else if (arr[mid] < target) {
			start = mid + 1;
		} else {
			end = mid - 1;
			first = mid;
		}
	}

	//Find last index by changing the start point when element == target
	start = 0;
	end = arr.length - 1;
	int last = -1;

	while (start <= end) {
		int mid = (start + end) / 2;

		if (arr[mid] > target) {
			end = mid - 1;
		} else if (arr[mid] < target) {
			start = mid + 1;
		} else {
			start = mid + 1;
			last = mid;
		}
	}

	System.out.println(first);
	System.out.println(last);
}

}