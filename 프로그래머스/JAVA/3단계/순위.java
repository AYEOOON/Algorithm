/*

1. 승패 정보를 그래프 형태로 저장한다.
  - 각 선수(노드)가 다른 선수(노드)를 이겼는지 졌는지를 2차원 배열(graph)에 저장
  - graph[i][j] = 1 
      → i가 j를 이겼음
  - graph[i][j] = -1 
      → i가 j에게 졌음
  - graph[i][j] = 0 
      → 모름 (초기 상태)

2. 플로이드-워셜 알고리즘을 이용해 승패 관계를 유추한다.
  - 특정 선수를 중간 선수로 거쳐 승패 관계를 더 알 수 있는지 확인
  
  - 만약 A가 B를 이겼고(B > C), B가 C를 이겼다면(A > B)
      → A는 C도 이긴 것(A > C)으로 처리
  - 반대로 A가 B에게 졌고(B > A), B가 C에게 졌다면(C > B)
      → A는 C에게도 진 것(C > A)으로 처리

3. 순위를 확정할 수 있는 선수의 수를 구한다.
  - 순위를 확정하려면 n-1명의 선수와 관계(이기거나 지거나)를 알아야 함
  - graph[i][j]가 1 또는 -1인 개수를 세어 n-1개라면 순위가 확정된 것으로 판단

*/

import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        // 1. 승패 정보를 그래프에 저장
        int[][] graph = new int[n+1][n+1];
        
        for(int[] result: results){
            int winner = result[0];
            int loser = result[1];
            graph[winner][loser] = 1;
            graph[loser][winner] = -1;
        }
        
        // 2. 플로이드-워셜 알고리즘 적용
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                for(int k = 0; k <= n; k++){
                    if(graph[i][k] == 1 && graph[k][j] == 1){
                        graph[i][j] = 1;
                        graph[j][i] = -1;
                    }
                    if(graph[i][k] == -1 && graph[k][j] == -1){
                        graph[i][j] = -1;
                        graph[j][i] = 1;
                    }
                }
            }
        }
    
        // 3. 순위를 확정할 수 있는 선수 확인
        for(int i = 1; i <= n; i++){
            int cnt = 0;
            for(int j = 1; j <= n; j++){
                if(graph[j][i] == 1 || graph[j][i] == -1){
                    cnt++;
                }
            }
            if(cnt == n-1){
                answer++;
            }
        }
        return answer;
    }
}
