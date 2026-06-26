/*
https://school.programmers.co.kr/learn/courses/30/lessons/12971

[문제 설명]
원형으로 연결된 스티커가 주어진다. 
스티커를 하나 선택하면 양옆에 인접한 스티커는 사용할 수 없게 된다. 
뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 선택했을 때의 최대값을 구하는 문제이다. 

[풀이 아이디어]
처음에는 어떤 스티커를 선택했는지 인덱스를 저장하면서 풀어보려고 했지만, 문제에서 요구하는 것은 선택한 스티커 목록이 아니라 최대 합이다.
따라서 각 위치까지 고려했을 때의 최대 합만 저장하는 DP를 사용할 수 있다. 

1. 선형 배열인 경우
만약 스티커가 일렬로 배치되어 있다면 다음과 같은 점화식을 사용할 수 있다.

dp[i] = Math.max(
    dp[i - 1],              // 현재 스티커를 선택하지 않는 경우
    dp[i - 2] + sticker[i]  // 현재 스티커를 선택하는 경우
);

즉, (1)현재 스티커를 선택하지 않으면 이전 최대값을 유지하고, (2)현재 스티커를 선택하면 바로 이전 스티커는 선택할 수 없으므로 dp[i-2]에 현재 값을 더한다.

2. 원형 배열 처리
이 문제의 핵심은 스티커가 원형이라는 점이다. 
첫 번째 스티커와 마지막 스티커가 인접해 있으므로 두 개를 동시에 선택할 수 없다. 
따라서 경우를 두 개로 나누어 생각한다.

Case 1: 첫 번째 스티커를 선택하는 경우
- 첫 번째 스티커를 선택했다면 마지막 스티커는 선택할 수 없다. (0 ~ n-2 까지만 고려)

Case 2: 첫 번째 스티커를 선택하지 않는 경우
- 첫 번째 스티커를 선택하지 않았다면 마지막 스티커를 선택할 수 있다. (1 ~ n-1 까지 고려)

[배운 점]
- 원형 구조의 DP 문제는 첫 번째 원소를 선택하는 경우와 선택하지 않는 경우로 분리하면 해결할 수 있다.
- DP는 선택한 경로를 모두 저장하는 것이 아니라 현재까지의 최적해만 저장해도 충분한 경우가 많다.
- 점화식을 세우는 것보다도 상태를 어떻게 정의할 것인지가 더 중요하다.
- 이 문제는 선형 배열의 "집 털기(House Robber)" 문제를 원형 배열로 확장한 형태이다.
*/

import java.util.*;

class Solution {
    public int solution(int sticker[]) {
        int n = sticker.length;

        if (n == 1) return sticker[0];

        int[] case1 = new int[n];
        int[] case2 = new int[n];

        // 첫 번째 스티커를 포함하는 경우
        case1[0] = sticker[0];
        case1[1] = Math.max(sticker[0], sticker[1]);

        for (int i = 2; i < n - 1; i++) {
            case1[i] = Math.max(case1[i - 1], case1[i - 2] + sticker[i]);
        }

        // 첫 번째 스티커를 포함하지 않는 경우
        case2[0] = 0;
        case2[1] = sticker[1];

        for (int i = 2; i < n; i++) {
            case2[i] = Math.max(case2[i - 1], case2[i - 2] + sticker[i]);
        }

        return Math.max(
            Arrays.stream(case1).max().getAsInt(),
            Arrays.stream(case2).max().getAsInt()
        );
    }
}
