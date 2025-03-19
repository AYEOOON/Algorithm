/*

1. 문제 분석:
  - 로봇은 시작점에서 출발해 상, 하, 좌, 우로 이동
  - 이동은 장애물에 부딪히거나 게임판의 경계에 도달할 때까지 미끄러짐
  - 목표 지점에 도달하는 최단 이동 횟수를 구하는 문제

2. 알고리즘:
  - BFS (Breadth-First Search): BFS는 최단 경로 문제를 해결할 때 유용한 알고리즘이다.
  - BFS는 시작점에서부터 인접한 노드를 차례대로 탐색하여, 목표 지점에 도달하는 첫 번째 경로가 최단 경로임을 보장한다.
  - 각 이동은 미끄러지며 한 번에 여러 칸을 이동하므로, 각 이동을 반복해서 미끄러질 때까지 처리해야 함.

3. 방향:
  - BFS 큐에 위치를 저장하고, 상, 하, 좌, 우 방향으로 미끄러지며 이동
  - 이동 시 목표 지점에 도달하면, 현재까지의 이동 횟수를 반환
  - 목표에 도달할 수 없는 경우, -1을 반환

*/

import java.util.*;

class Solution {
    public int solution(String[] board) {
        int n = board.length; // 보드의 세로 크기 (행 수)
        int m = board[0].length(); // 보드의 가로 크기 (열 수)
        
        // 방문 여부를 기록할 배열
        boolean[][] visited = new boolean[n][m];
        
        // 상, 하, 좌, 우 방향 벡터
        int[] dx = {0, 0, -1, 1}; // 상, 하, 좌, 우의 x축 변화
        int[] dy = {1, -1, 0, 0}; // 상, 하, 좌, 우의 y축 변화

        // BFS 탐색을 위한 큐 (큐에 위치(x, y)와 현재까지의 이동 횟수(cnt)를 저장)
        Queue<int[]> Q = new LinkedList<>();
        
        // 시작점(R)을 찾아 큐에 넣고 방문 처리
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(board[i].charAt(j) == 'R'){ // 'R'을 찾으면
                    Q.offer(new int[]{i, j, 0}); // (x, y, 이동 횟수 0) 큐에 넣음
                    visited[i][j] = true; // 시작 위치 방문 처리
                }
            }
        }
        
        // BFS 탐색 시작
        while(!Q.isEmpty()){
            int[] tmp = Q.poll(); // 큐에서 현재 위치와 이동 횟수 가져옴
            int x = tmp[0]; // 현재 위치의 x 좌표
            int y = tmp[1]; // 현재 위치의 y 좌표
            int cnt = tmp[2]; // 현재까지의 이동 횟수
            
            // 목표 지점(G)에 도달하면 현재까지의 이동 횟수 반환
            if(board[x].charAt(y) == 'G'){
                return cnt; // 목표 지점에 도달했으므로 이동 횟수 반환
            }
            
            // 상, 하, 좌, 우로 이동을 시도
            for(int i = 0; i < 4; i++){
                int nx = x; // 새로운 x 좌표
                int ny = y; // 새로운 y 좌표
                
                // 해당 방향으로 미끄러지며 이동
                while(true){
                    int tx = nx + dx[i]; // 한 칸 이동한 x 좌표
                    int ty = ny + dy[i]; // 한 칸 이동한 y 좌표
                    
                    // 벽이나 장애물에 부딪히거나 경계를 벗어나면 멈춤
                    if (tx < 0 || tx >= n || ty < 0 || ty >= m || board[tx].charAt(ty) == 'D') {
                        break; // 벽이나 장애물에 도달했으면 더 이상 이동할 수 없음
                    }
                    
                    // 미끄러져서 계속 이동
                    nx = tx;
                    ny = ty;
                }
                
                // 새로운 위치가 아직 방문되지 않은 곳이라면
                if(!visited[nx][ny]){
                    visited[nx][ny] = true; // 방문 처리
                    Q.offer(new int[]{nx, ny, cnt + 1}); // 새로운 위치를 큐에 추가 (이동 횟수 1 증가)
                }
            }
        }
        
        // 목표 지점에 도달할 수 없다면 -1 반환
        return -1;
    }
}
