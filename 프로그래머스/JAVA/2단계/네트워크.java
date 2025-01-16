class Solution {
    int answer = 0;
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                answer++;
                dfs(i, computers, n, visited);
            }
        }
        return answer;
    }
    public void dfs(int idx, int[][] computers, int n, boolean[] visited){
        visited[idx] = true;
        for(int i = 0; i<n; i++){
            if(computers[idx][i] == 1 && !visited[i]){
                dfs(i, computers, n, visited);
            }
        }
    }
}
