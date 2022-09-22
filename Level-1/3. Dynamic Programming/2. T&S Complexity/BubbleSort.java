import java.util.Scanner;

class BubbleSort {

	public static void bubbleSort(int[] arr) {

		/*
		Time complexity: O(n*n)
		Space complexity: O(1)
		*/

		//Outer loop for number of iterations
		for (int i = 1; i <= arr.length - 1; i++) {

			//Inner loop for comparing elements
			for (int j = 0; j < arr.length - i; j++) {
				if (arr[j + 1] < arr[j]) {
					int temp = arr[j + 1];
					arr[j + 1] = arr[j];
					arr[j] = temp;
				}
			}
		}
	}

	public static void printArr(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
	}
	
	public static void main (String[] args) {
		
		//Take input
		Scanner input = new Scanner(System.in);
		int size = input.nextInt();
		int[] arr = new int[size];

		for (int i = 0; i < size; i++) {
			arr[i] = input.nextInt();
		}

		bubbleSort(arr);
		printArr(arr);
	}
}