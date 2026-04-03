/*
https://school.programmers.co.kr/learn/courses/30/lessons/178870
: 양의 정수로 이루어진 배열 sequence가 주어질 때, 연속된 부분 수열의 합이 k가 되는 구간 [start, end]를 구하는 문제

[초기 접근]
- 가능한 모든 구간을 탐색하면서 합을 직접 계산
- (start, end)를 정하고, 해당 구간의 합을 구하는 방식
👉 구간을 하나 계산할 때마다 합을 다시 구함, N이 커지면 시간 초과 발생

[개선한 접근: 슬라이딩 윈도우]
- 합을 매번 새로 계산하지 않고 유지한다
- 구간을 확장하거나 축소하면서 조건을 만족시키는 구간을 찾는다

1. right를 증가시키며 구간 확장
2. 현재 합(sum)이 k보다 크면 left를 증가시키며 축소
3. 합이 k가 되면 정답 후보 갱신

[결론]
1. 단순 탐색 → 누적합 → 투포인터로 개선
2. 연속된 구간 + 합 조건 문제는 슬라이딩 윈도우가 가장 효율적인 해결 방법이다
3. 배열이 양수로 이루어져 있을 때 특히 효과적이다
*/

class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
    
        int left = 0;
        int sum = 0;
        
        int minLen = Integer.MAX_VALUE;
        
        for (int right = 0; right < sequence.length; right++){
            sum += sequence[right];
            
            while (sum > k){
                sum -= sequence[left++];
            }
            
            if (sum == k){
                if ((right - left) < minLen){
                    answer[0] = left;
                    answer[1] = right;
                }
                minLen = right - left;
            }
        }
        return answer;
    }
}
