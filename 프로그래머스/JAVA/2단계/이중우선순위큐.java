import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        ArrayList<Integer> Q = new ArrayList<>();
        
        for(String op: operations){
            String[] arr = op.split(" ");
            if(arr[0].equals("I")) {
                Q.add(Integer.parseInt(arr[1]));
                Collections.sort(Q);
            }
            else if(arr[0].equals("D") && !Q.isEmpty()){
                if(arr[1].equals("-1")){
                    Q.remove(0);
                }else{
                    Q.remove(Q.size()-1);
                }
            }
        }
        if(!Q.isEmpty()){
            answer[0] = Q.get(Q.size()-1);
            answer[1] = Q.get(0);
        }
        return answer;
    }
}
