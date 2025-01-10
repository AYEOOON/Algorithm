/*
<소수 배열 초기화 메소드(initPrimeArray)>
  - initPrimeArray는 max까지의 숫자에 대해 소수 여부를 판별해 isPrime 배열에 저장합니다.
  - 에라토스테네스의 체 알고리즘을 사용하여 소수 판별을 효율적으로 수행합니다.
  - isPrime[i]가 true이면 i는 소수입니다. false로 변경된 값은 소수가 아닙니다.
    
<순열 생성 및 소수 판별 메소드(findCombinations)>
  - findCombinations는 prefix를 통해 현재까지의 숫자 조합을 나타내며, str은 사용 가능한 숫자입니다.
  - prefix가 비어 있지 않으면, 숫자로 변환하여 소수 여부를 확인합니다.
  - prefix와 str을 활용해 재귀적으로 모든 가능한 조합을 생성합니다.
  - 발견된 소수는 uniqueNumbers에 저장됩니다. => 동일한 값을 넣지 않기 위해 Set 자료구조를 이용합니다.
  
<solution 메소드>
  - maxNum은 입력된 숫자 문자열의 길이에 따라 가장 큰 숫자를 계산합니다 (10^length).
  - initPrimeArray를 통해 maxNum까지의 소수 여부를 미리 계산합니다.
  - findCombinations 메서드를 호출해 모든 가능한 숫자 조합을 탐색하고 소수를 찾습니다.
  - uniqueNumbers.size()를 반환하여 발견된 소수의 개수를 출력합니다.
*/

import java.util.*;

class Solution {
    boolean[] isPrime;
    Set<Integer> uniqueNumbers = new HashSet<>();
    
    public void initPrimeArray(int max) {
        isPrime = new boolean[max + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i <= max; i++) {
            if (isPrime[i]) {
                for (int j = i * 2; j <= max; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }

    public void findCombinations(String prefix, String str) {
        if (!prefix.isEmpty()) {
            int num = Integer.parseInt(prefix);
            if (isPrime[num]) {
                uniqueNumbers.add(num);
            }
        }
        for (int i = 0; i < str.length(); i++) {
            findCombinations(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1));
        }
    }

    public int solution(String numbers) {
        int maxNum = (int) Math.pow(10, numbers.length());
        initPrimeArray(maxNum);

        // 모든 조합을 탐색
        findCombinations("", numbers);

        return uniqueNumbers.size();
    }
}
