import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    
    Scanner input = new Scanner(System.in);
    int matArows = input.nextInt();
    int matAcols = input.nextInt();
    
    int[][] matA = new int[matArows][matAcols];
    for (int i = 0; i < matArows; i++) {
        for (int j = 0; j < matAcols; j++) {
            matA[i][j] = input.nextInt();
        }
    }

    int matBrows = input.nextInt();
    int matBcols = input.nextInt();
    
    int[][] matB = new int[matBrows][matBcols];
    for (int i = 0; i < matBrows; i++) {
        for (int j = 0; j < matBcols; j++) {
            matB[i][j] = input.nextInt();
        }
    }

    if (matAcols != matBrows) {
        System.out.println("Invalid input");
    } else {
        multiplyMatrices(matA, matB);
    }
 }

 public static void multiplyMatrices(int[][] matA, int[][] matB) {
    int matCrows = matA.length;
    int matCcols = matB[0].length;
    int[][] matC = new int[matCrows][matCcols];
 }


}