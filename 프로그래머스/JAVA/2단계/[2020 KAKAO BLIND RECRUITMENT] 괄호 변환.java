/*
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
*/

import java.util.*;

class Solution {
    // 균형잡힌 문자열 만드는 함수
    public String make_balance(String w){
        if(w.isEmpty()) return w;
        int idx = 0;
        int openCount = 0, closeCount = 0;
        StringBuilder u = new StringBuilder();
        
        while(idx < w.length()){
            char c = w.charAt(idx);
            u.append(c);
            
            if(c == '(') openCount++;
            else if(c == ')') closeCount++;
        
            idx++;
            
            if(openCount==closeCount) break;

        }
        return u.toString();
    }
    
    // 올바른 문자열인지 확인하는 함수
    public boolean check_right(String u){
        Stack<Character> stck = new Stack<>();
        for(char c: u.toCharArray()){
            if (c=='('){
                stck.push('(');
            }else{
                if(stck.isEmpty()) return false;
                stck.pop(); 
            }
        }
        return stck.isEmpty();
    }
    
    // 문자열 뒤집는 함수
    public String back(String u){
        StringBuilder tmp = new StringBuilder();
        for(char c: u.toCharArray()){
            tmp.append(c=='(' ? ')' : '(');
        }
        return tmp.toString();
    }
    
    public String solution(String p) {
        // 1. 빈 문자열이면 반환
        if(p.isEmpty()) return p;
        
        // 2. 문자열 u, v로 분리
        String u = make_balance(p);
        String v = p.substring(u.length());

        // 3. u가 올바른 괄호 문자열인지 확인 후, v부터 다시 수행
        if(check_right(u)){
            return u+solution(v);
        }
        
        // 4. 아니라면
        String result = "(" + solution(v) + ")";  // 4-1~3
        u = u.substring(1, u.length()-1); // 4-4
        result += back(u); 
        return result;
    }
}
