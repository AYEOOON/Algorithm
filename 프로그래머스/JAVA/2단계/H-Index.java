class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int tmp = 0;
        while(tmp <= citations.length){
            int cnt = 0;
            for(int c: citations){
                if(c >= tmp) cnt++;
            }
            if(cnt <= tmp){
                answer = cnt;
                break;
            }
            tmp++;
        }
        return answer;
    }
}
