import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = bridge_length;
        ArrayList<Integer> cross = new ArrayList<>();
        for(int i = 0; i < bridge_length; i++){
            cross.add(0);
        }
        
        int idx = 0;
        while(idx < truck_weights.length){
            cross.remove(0);
            if(cross.stream().mapToInt(Integer::intValue).sum() + truck_weights[idx] <= weight){
                cross.add(truck_weights[idx]);
                idx++;
            }else{
                cross.add(0);
            }
            answer++;
        }
        return answer;
    }
}
