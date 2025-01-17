class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        for(int i = 0; i < prices.length-1; i++){
            int idx = i;
            while(idx < prices.length-1 && prices[i] <= prices[idx]){
                answer[i]++;
                idx++;
            }
        }
        return answer;
    }
}
