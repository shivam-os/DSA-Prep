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
    
    //Time Complexity: O(n^3)
    //First loop decides the starting point, second loop decides the end point
    //Third loop traverses all elements b/w the starting & end points
    
    for (int i = 0; i < size; i++) {
        for (int j = i; j < size; j++) {
            for (int k = i; k <= j; k++) {
                System.out.print(arr[k] + "\t");
            }
            System.out.println();
        }
    }
 }

}