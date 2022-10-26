import java.util.Scanner;

class Main {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		int size = input.nextInt();
		int[] arr = new int[size];

		for (int i = 0; i < size; i++) {
			arr[i] = input.nextInt();
		}

		//Space Complexity, Time Complexity: O(n)
		int[] inverse = new int[size];

		for (int i = 0; i < size; i++) {
			int value = arr[i];
			inverse[value] = i; 
		}

		for (int i = 0; i < size; i++) {
			System.out.println(inverse[i]);
		}
	}
}