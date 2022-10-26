import java.util.Scanner;

class Main {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		int size = input.nextInt();
		int[] arr = new int[size];

		for (int i = 0; i < size; i++) {
			arr[i] = input.nextInt();
		}

		//Reverse Array
		//Time Complexity: O(n)
		int start = 0;
		int end = size - 1;

		while (start < end) {
			int temp = arr[start];
			arr[start] = arr[end];
			arr[end] = temp;

			start++;
			end--;
		}

		for (int i = 0; i < size; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}