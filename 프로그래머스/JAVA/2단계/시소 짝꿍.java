/*
https://school.programmers.co.kr/learn/courses/30/lessons/152996

[문제 설명]
시소의 좌석은 중심으로부터 2m, 3m, 4m 위치에만 존재한다. 
두 사람이 마주 보고 앉았을 때 무게 × 거리가 서로 같으면 시소가 평형을 이루므로 시소 짝꿍이 된다.

주어진 몸무게 배열에서 시소 짝꿍이 될 수 있는 모든 사람 쌍의 개수를 구하는 문제

시소가 평형을 이루는 조건은 몸무게1 × 거리1 = 몸무게2 × 거리2이다. 
거리로 사용할 수 있는 값이 2, 3, 4뿐이므로 가능한 몸무게 비율은 1:1, 2:3, 1:2, 3:4 네 가지 경우만 존재하게 된다.

[풀이 아이디어]
사람 수가 최대 100,000명이므로 모든 쌍을 비교하는 O(N²) 방식은 사용할 수 없다.
먼저 몸무게를 오름차순으로 정렬하여 현재 몸무게보다 큰 값은 아직 처리하지 않은 상태로 만든다.
  -> 정렬하지 않으면 입력 순서가 보장되지 않기 때문에 짝꿍을 놓칠 수 있다. 

현재 몸무게를 w라고 할 때 짝꿍이 될 수 있는 이전 몸무게는 w, w×2/3, w/2, w×3/4이다. 
이 값들이 정수인 경우에만 HashMap에서 해당 몸무게가 이전에 몇 번 등장했는지 확인하고 그 개수를 정답에 더한다.

이후 현재 몸무게의 등장 횟수를 HashMap에 저장한 후 각 몸무게를 한 번만 처리하면서 짝꿍의 수를 계산할 수 있다.

핵심은 시소의 평형 조건을 몸무게 비율 문제로 변환하고, 
가능한 비율이 4가지뿐이라는 점을 이용해 HashMap으로 이전에 등장한 몸무게의 개수를 빠르게 조회하는 것이다.
*/

import java.util.*;

class Solution {
    public long solution(int[] weights) {
        Map<Integer, Integer> count = new HashMap<>();
        Arrays.sort(weights);
        long answer = 0;
        
        for (int w: weights){
            // 같은 무게
            answer += count.getOrDefault(w, 0);
            // 2:3
            if (w*2%3 == 0){
                answer += count.getOrDefault(w*2/3, 0);
            }
            // 2:4
            if (w%2 == 0){
                answer += count.getOrDefault(w*2/4, 0);
            }
            // 3:4
            if (w*3%4 == 0){
                answer += count.getOrDefault(w*3/4, 0);
            }
            count.put(w, count.getOrDefault(w, 0) + 1);
        }
        return answer;
    }
}
