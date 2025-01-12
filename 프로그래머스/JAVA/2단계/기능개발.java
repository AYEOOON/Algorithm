import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        ArrayList<Integer> remain = new ArrayList<>();
        for(int i = 0; i < progresses.length; i++){
            remain.add((int)Math.ceil((double)(100-progresses[i])/speeds[i]));
        }
        int cnt = 0;
        int max = remain.get(0); 
        for(int r: remain){
            if(r > max){
                answer.add(cnt);
                cnt = 0;
                max = r;
            }
            cnt++;
        }
        answer.add(cnt);
        return answer;
    }
}
