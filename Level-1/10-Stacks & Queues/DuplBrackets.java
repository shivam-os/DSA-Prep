import java.io.*;
import java.util.*;

public class DuplBrackets {

    public static void main(String[] args) throws Exception {
        
        /*
        Time Complexity: O(n)
        Space Coplexity: O(1)
        */
        
        //Take input
        Scanner input = new Scanner(System.in);
        String str = input.nextLine();
        
        Stack<Character> st = new Stack<Character>();
        
        //Iterate through the string expression
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            
            if (ch == ')') {
                if (st.peek() == '(') {
                    System.out.println(true);
                    return;
                } else {
                    while (st.peek() != '(') {
                        st.pop();
                    }
                    st.pop();
                }
            } else {
                st.push(ch);
            }
        }
        
        System.out.println(false);
    }

}