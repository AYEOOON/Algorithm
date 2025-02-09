import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> idx = new LinkedList<>();
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < priorities.length; i++){
            idx.offer(i);
            q.offer(priorities[i]);
        }
        while(!q.isEmpty()){
            int max = Collections.max(q);
            int cur_process = q.poll();
            int cur_idx = idx.poll();
            
            if(cur_process < max){
                q.offer(cur_process);
                idx.offer(cur_idx);
            }else{
                answer++;
                if(cur_idx == location){
                    break;
                }
            }
        }
        return answer;
    }
}
