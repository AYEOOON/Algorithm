/*
방향(dx, dy)을 정해놓고 아래 → 오른쪽 → 왼쪽 위 순으로 반복 이동

한 방향으로 갈 때 이동 횟수를 세다가, 다 채우면 방향을 바꿔 이동

이동 거리는 한 방향을 채울 때마다 1씩 줄어듦

최종적으로 0이 아닌 숫자들만 answer 리스트에 담아서 반환
*/

import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        // 방향을 정의: 아래(1,0), 오른쪽(0,1), 왼쪽위(-1,-1)
        int[] dx = {1, 0, -1};  
        int[] dy = {0, 1, -1}; 
        
        // n x n 크기의 2차원 배열 생성
        int[][] arr = new int[n][n];
        
        int idx = 0;  // 방향 전환용 인덱스 (0: 아래, 1: 오른쪽, 2: 왼쪽 위)
        int x = 0;    // 현재 위치 x좌표
        int y = 0;    // 현재 위치 y좌표
        int go = n;   // 현재 이동해야 할 거리 (처음엔 n부터 시작)
        int cnt = 1;  // 현재 이동 거리 체크용
        int num = 1;  // 채워 넣을 숫자 (1부터 시작)

        // 채워야 할 거리가 남아 있는 동안 반복
        while(go > 0){
            // 현재 이동 거리(cnt)가 목표 이동 거리(go)에 도달하면
            if(cnt == go){
                go--;          // 목표 이동 거리를 1 감소
                idx++;         // 방향 전환
                cnt = 0;       // 이동 거리 리셋
            }
            arr[x][y] = num++; // 현재 위치에 숫자 채우기
            // 다음 이동
            x += dx[idx%3];    
            y += dy[idx%3];
            cnt++;             // 이동 거리 1 증가
        }

        // 배열에 채워진 값을 answer 리스트에 추가
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(arr[i][j] != 0){   // 0이 아닌 값만 추가
                    answer.add(arr[i][j]);
                }
            }
        }

        return answer;
    }
}
