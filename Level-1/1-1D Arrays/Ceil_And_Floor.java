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

    CeilAndFloor(arr, target);
 }

public static void CeilAndFloor(int[] arr, int target) {

	//Time Complexity: O(log n)
	//Based on Binary Search

	int start = 0;
	int end = arr.length - 1;
	int ceil = 0;
	int floor = 0;

	while (start <= end) {
		int mid = (start + end) / 2;

		if (arr[mid] > target) {
			end = mid - 1;
			ceil = arr[mid];
		} else if (arr[mid] < target) {
			start = mid + 1;
			floor = arr[mid];
		} else {
			ceil = arr[mid];
			floor = arr[mid];
			break;
		}
	}

	System.out.println(ceil);
	System.out.println(floor);
}

}