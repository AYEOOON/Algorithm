/*
https://school.programmers.co.kr/learn/courses/30/lessons/42895
: 숫자 N과 목표값 number가 주어질 때, 사칙연산과 괄호를 이용하여 number를 만들 수 있는 최소 N 사용 횟수를 구하는 문제

[초기 접근]
처음에는 모든 수식을 직접 만들어보는 완전 탐색을 떠올릴 수 있다. 
하지만, 경우의 수가 매우 많아지고, 중복 계산이 발생하기 때문에 비효율적이다.

[재해석]
이 문제의 핵심은 "몇 번 사용했을 때 어떤 값을 만들 수 있는가" 이다.
즉, 사용 횟수 기준으로 경우를 확장하는 문제이다.

[핵심 아이디어]
dp[i] = N을 i번 사용해서 만들 수 있는 모든 값으로 정의한다.
- i는 1부터 8까지
- 각 dp[i]는 Set으로 관리한다.

[왜 Set을 사용하는가]
- 같은 값이 여러 번 생성되고, 
- 이 문제에서 "값"만 필요하고, "과정"은 필요없다. 
- 중복 제거로 성능 향상까지 할 수 있다.
*/

import java.util.*;

class Solution {
    public int solution(int N, int number) {
        int answer = -1;
        List<Set<Integer>> dp = new ArrayList<>();
        
        for (int i = 0; i <= 8; i++) {
            dp.add(new HashSet<>());
        }

        // 초기값 설정
        int num = 0;
        for (int i = 1; i <= 8; i++){
            num = num*10+N;
            dp.get(i).add(num);
        }

        // dp[i]는 다음과 같이 구성된다. dp[i] = dp[j] 와 dp[i-j]의 모든 조합 (1 ≤ j < i)
        for (int i = 1; i <= 8; i++){
            for (int j = 1; j < i; j++){
                for (int a : dp.get(j)){
                    for (int b : dp.get(i-j)){  // 각 조합에 대해 연산 수행
                        dp.get(i).add(a + b); 
                        dp.get(i).add(a - b);
                        dp.get(i).add(a * b);
                        
                        if (b!=0){
                            dp.get(i).add(a / b);
                        }
                    }
                }
            }
            if (dp.get(i).contains(number)){
                return i;
            }
        }
        return answer;
    }
}
