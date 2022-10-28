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
    
    int position = BinarySearch(arr, target);
    System.out.println(position);
 }

public static int BinarySearch(int[] arr, int target) {

	//Time Complexity: O(log n)

	int start = 0;
	int end = arr.length - 1;

	while (start <= end) {
		int mid = (start + end) / 2;

		if (arr[mid] > target) {
			end = mid - 1;
		} else if (arr[mid] < target) {
			start = mid + 1;
		} else {
			return mid;
		}
	}

	return -1;
}

}