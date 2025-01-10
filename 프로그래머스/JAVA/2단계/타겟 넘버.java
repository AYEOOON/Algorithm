// 찝찝하게 푼 문제
// 힌트를 너무 많이 보고 풀어서 그런 듯

class Solution {
    int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, 0, target);
        return answer;
    }
    public void dfs(int[] numbers, int idx, int sum, int target){
        if(idx == numbers.length){
            if(sum == target) answer++;
        }else{
            dfs(numbers, idx+1, sum+numbers[idx], target);
            dfs(numbers, idx+1, sum-numbers[idx], target);
        }
    }
}
