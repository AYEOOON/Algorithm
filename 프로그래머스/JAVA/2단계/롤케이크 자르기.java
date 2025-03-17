/*

1. 초기 세팅
  - 동생(dongsangMap)이 모든 토핑을 가지고 시작
  - 형(hyungSet)은 빈 상태에서 시작

2. 형이 하나씩 토핑을 가져갈 때마다 업데이트
  - 형이 Set에 추가 (중복 방지)
  - 동생의 Map에서 해당 토핑 개수 감소
  - 개수가 0이 되면 완전히 제거

3. 매 순간 형과 동생의 토핑 종류 개수를 비교
  - hyungSet.size() == dongsangMap.size()이면 경우의 수 증가

중요: 각자가 가진 토핑의 갯수가 아닌 가짓 수에 집중!
*/

import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        int n = topping.length;

        HashSet<Integer> hyungSet = new HashSet<>();  // 형이 가진 토핑 종류
        HashMap<Integer, Integer> dongsangMap = new HashMap<>(); // 동생이 가진 토핑 개수

        // 처음에 동생이 모든 토핑을 가지고 있도록 설정
        for (int t : topping) {
            dongsangMap.put(t, dongsangMap.getOrDefault(t, 0) + 1);
        }

        // 형이 하나씩 가져가면서 동생의 토핑 개수를 줄임
        for (int i = 0; i < n - 1; i++) {
            hyungSet.add(topping[i]);  // 형이 토핑을 추가
            dongsangMap.put(topping[i], dongsangMap.get(topping[i]) - 1);

            // 동생 쪽에서 해당 토핑 개수가 0이면 제거
            if (dongsangMap.get(topping[i]) == 0) {
                dongsangMap.remove(topping[i]);
            }

            // 형과 동생의 토핑 종류 개수가 같으면 경우의 수 증가
            if (hyungSet.size() == dongsangMap.size()) {
                answer++;
            }
        }
        return answer;
    }
}
