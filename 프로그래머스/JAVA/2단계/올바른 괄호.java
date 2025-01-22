import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<String> stck = new Stack<>();
        
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(ch == '('){
                stck.push("(");
            }else if(ch == ')'){
                if(stck.isEmpty()){
                    return false;
                }
                stck.pop();
            }
        }
        return stck.isEmpty();
    }
}
