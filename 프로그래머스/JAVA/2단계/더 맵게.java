import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> Q = new PriorityQueue<>();
        for(int n: scoville){
            Q.offer(n);
        }
        while(Q.peek() < K && Q.size() > 1){
            Q.offer(Q.poll()+(Q.poll()*2));
            answer++;
        }
        return Q.peek() >= K ? answer : -1;
    }
}
