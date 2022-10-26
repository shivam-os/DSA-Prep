import java.util.Scanner;

class Main {
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		int size = input.nextInt();
		int[] arr = new int[size];

		for (int i = 0; i < size; i++) {
			arr[i] = input.nextInt();
		}

		//Time complexity: O(n)
		int target = input.nextInt();

		int position = LinearSearch(arr, target);
		System.out.println(position);
	}

	public static int LinearSearch(int[] arr, int target) {
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == target) {
				return i;
			}
		}
		return -1;
	}
}