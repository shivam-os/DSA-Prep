import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    
    //Time Complexity: O(n + m*n)
    //Here, m = highest floor
    
    Scanner input = new Scanner(System.in);
    int size = input.nextInt();
    int[] arr = new int[size];
    
    for (int i = 0; i < size; i++) {
        arr[i] = input.nextInt();
    }
    
    //Finding the highest floor
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    
    //Place brick only when height is equal or greater otherwise place black space
    for (int floor = max; floor > 0; floor--) {
        for (int j = 0; j < size; j++) {
            if (arr[j] >= floor) {
                System.out.print("*\t");
            } else {
                System.out.print("\t");
            }
        }
        System.out.println();
    }
    
 }

}