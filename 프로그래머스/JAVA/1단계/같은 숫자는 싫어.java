import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> num = new ArrayList<>();
        num.add(arr[0]);
        for(int i = 1; i < arr.length; i++){
            if(num.get(num.size()-1) != arr[i]){
                num.add(arr[i]);
            }
        }
        int[] answer = new int[num.size()];
        for(int i = 0; i < num.size(); i++){
            answer[i] = num.get(i);
        }
        return num.toArray(new int[num.size()]);
    }
}
