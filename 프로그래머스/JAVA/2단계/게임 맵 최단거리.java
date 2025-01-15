import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int n = maps.length;
        int m = maps[0].length;
        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};
        
        Queue<int[]> Q = new LinkedList<>();
        Q.offer(new int[]{0,0,1});
        
        while(!Q.isEmpty()){
            int[] tmp = Q.poll();
            int x = tmp[0];
            int y = tmp[1];
            int cnt = tmp[2];
            if(x == n-1 && y == m-1){
                return cnt;
            }
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0<=nx && nx<n && 0<=ny && ny<m && maps[nx][ny] == 1){
                    maps[nx][ny] = 0;
                    Q.offer(new int[]{nx, ny, cnt+1});
                }
            }
        }
        return -1;
    }
}
