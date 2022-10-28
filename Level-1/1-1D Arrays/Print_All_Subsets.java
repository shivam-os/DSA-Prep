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

    //Time complexity: O(m*n), where m is 2^arr.length
    
    //For 2^n subsets, where each number corresponds to a specific set
    int limit = (int)Math.pow(2, arr.length);
    
    //First loop is for getting the numbers one by one
    for (int i = 0; i < limit; i++) {
        int temp = i;
        String set = "";
        
        //Second loop is for getting the array elements. It's running in reverse to get correct order of subset.
        for (int j = arr.length - 1; j >= 0; j--) {

        	//Find binary & place "-" if remainder is 0 otherwise place the element
            int rem = temp % 2;
            temp = temp / 2;
            
            if (rem == 0) {
                set = "-\t" + set;
            } else {
                set = arr[j] + "\t" + set;
            }
        }
        System.out.println(set);
    }
 }

}