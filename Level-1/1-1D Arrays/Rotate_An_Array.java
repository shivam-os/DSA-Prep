import java.util.Scanner;

class Main {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		int size = input.nextInt();
		int[] arr = new int[size];

		for (int i = 0; i < size; i++) {
			arr[i] = input.nextInt();
		}

		int k = input.nextInt();

		//Reduce the value of k to handle cases where k > size
		k = k % size;

		rotate(arr, k);

		for (int i = 0; i < size; i++) {
			System.out.print(arr[i] + " ");
		}
	}

	public static void rotate(int[] arr, int k) {
		//k = -1 is same as k = 4. Therefore, find the corresponding positive value of k
		if (k < 0) {
			k = k + arr.length;
		}

		//Divide the array into two parts. P1: 0-k to size-k-1, P2: size-k to size-1
		reverse(arr, 0, arr.length - k - 1); //Reverse the first part
		reverse(arr, arr.length - k, arr.length - 1); //Reverse the second part
		reverse(arr, 0, arr.length - 1); //Reverse the whole array
	}

	public static void reverse(int[] arr, int i, int k) {
		int start = i;
		int end = k;

		while (start < end) {
			int temp = arr[start];
			arr[start] = arr[end];
			arr[end] = temp;

			start++;
			end--;
		}
	}
}