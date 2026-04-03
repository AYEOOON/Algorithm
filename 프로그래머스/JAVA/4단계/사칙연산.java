/*
https://school.programmers.co.kr/learn/courses/30/lessons/1843
:숫자와 연산자(+, -)로 이루어진 수식이 주어질 때, 괄호를 적절히 배치하여 만들 수 있는 결과 중 최댓값을 구하는 문제.

연산 순서에 따라 결과가 달라짐
모든 경우의 수를 고려해야 함

[초기 접근]
처음에는 모든 괄호 경우를 직접 만들어서 계산하려고 했다.
- 가능한 모든 연산 순서를 탐색
- 각각 계산하여 최댓값 선택
하지만 이 방법은 경우의 수가 매우 많아져 비효율적이다.

[문제 재해석]
이 문제는 "괄호를 어디에 칠 것인가"가 아니라
-> "수식을 여러 구간으로 나누는 문제"
로 볼 수 있다.

[핵심 아이디어]
하나의 구간 i ~ j를 계산할 때, "i ~ k"  op  "k+1 ~ j" 와 같이 나눌 수 있다.
즉, 전체 수식은 작은 구간들의 결과를 조합하여 만들어진다.

[왜 DP를 사용하는가]
같은 구간을 여러 번 계산하게 되므로, 이미 계산한 결과를 저장하여 재사용해야 한다.

[DP 정의]
dpMax[i][j] : i ~ j 구간에서 만들 수 있는 최댓값
dpMin[i][j] : i ~ j 구간에서 만들 수 있는 최솟값

[왜 최대와 최소 모두를 저장해야 하는가]
뺄셈(-) 때문이다.

A - B 경우일 때, 
최댓값을 만들기 위해서는
→ A는 최대, B는 최소로,

최솟값을 만들기 위해서는
→ A는 최소, B는 최대로 해야한다.

따라서 하나의 값만으로는 충분하지 않다.

[핵심 정리]
- 문제를 “괄호 배치”가 아니라 “구간 분할”로 바라본다
- 하나의 구간은 하나의 값이 아니라 값의 범위 (max, min) 를 가진다
- 결과는 작은 구간을 조합하여 만들어진다
*/

import java.util.*;

class Solution {
    public int solution(String arr[]) {
        List<Integer> nums = new ArrayList<>();
        List<String> ops = new ArrayList<>();

        // 전처리
        for (String s: arr){
            if (s.equals("+") || s.equals("-")){
                ops.add(s);
            }else{
                nums.add(Integer.parseInt(s));
            }
        }

        // 초기값 설정
        int n = nums.size();
        int[][] dpMAX = new int[n][n];
        int[][] dpMIN = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dpMAX[i], Integer.MIN_VALUE);
            Arrays.fill(dpMIN[i], Integer.MAX_VALUE);
        }
        for (int i = 0; i < n; i++) {
            dpMAX[i][i] = nums.get(i);
            dpMIN[i][i] = nums.get(i);
        }

        // 구간 i ~ j를 계산할 때, 모든 k에 대해 분할
        for (int len = 1; len < n; len++){
            for (int i = 0; i+len < n; i++){
                int j = i+len;
                for (int k = i; k < j; k++){
                    String op = ops.get(k);
                    
                    int leftMax = dpMAX[i][k];
                    int leftMin = dpMIN[i][k];
                    int rightMax = dpMAX[k+1][j];
                    int rightMin = dpMIN[k+1][j];
                    
                    if (op.equals("+")){
                        int max = leftMax + rightMax;
                        int min = leftMin + rightMin;

                        dpMAX[i][j] = Math.max(dpMAX[i][j], max);
                        dpMIN[i][j] = Math.min(dpMIN[i][j], min);
                    }else{
                        int max = leftMax - rightMin;
                        int min = leftMin - rightMax;

                        dpMAX[i][j] = Math.max(dpMAX[i][j], max);
                        dpMIN[i][j] = Math.min(dpMIN[i][j], min);
                    }
                }
            }
        }
        return dpMAX[0][n-1];
    }
}
