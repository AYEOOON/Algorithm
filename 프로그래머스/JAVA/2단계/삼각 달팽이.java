import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        int[] dx = {1, 0, -1};
        int[] dy = {0, 1, -1};
        int[][] arr = new int[n][n];
        int idx = 0;
        int x = 0; 
        int y = 0;
        int go = n;
        int cnt = 1;
        int num = 1;
        while(go > 0){
            if(cnt == go){
                go--;
                idx++;
                cnt = 0;
            }
            arr[x][y] = num++;
            x += dx[idx%3];
            y += dy[idx%3];
            cnt++;
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(arr[i][j] != 0){
                    answer.add(arr[i][j]);
                }
            }
        }
        return answer;
    }
}
