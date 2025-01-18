import java.util.*;

class Solution {
    String[] words = {"A", "E", "I", "O", "U"};
    int Length = 5;
    public int solution(String word) {
        ArrayList<String> output = new ArrayList<>();
        for(int i = 0; i < words.length; i++){
            dfs(output, words[i]);
        }
        Collections.sort(output);
        return output.indexOf(word)+1;
    }
    
    public void dfs(ArrayList<String> output, String str){
        if(str.length() > Length) return;
        if(!output.contains(str)) output.add(str);
        for(int i = 0; i < words.length; i++){
            dfs(output, str+words[i]);
        }
    }
}
