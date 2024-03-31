"""
당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
알아볼 수 없는 번호를 0으로 표기하기로 하고, 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
"""
"""
1. 맞춘 갯수와 인덱스를 이용하여 순위 배열 생성
2. 첫번째 for 문으로 0의 갯수 세리기
3. 두번째 for 문으로 맞는 갯수 세리기
4. 맞춘 갯수의 rank인덱스로 순위 저장하기
"""

# 내 풀이
import java.util.Arrays;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] guess = {0,0};
        int[] answer = new int[2]; # 새로운 배열 생성
        int[] rank = {6,6,5,4,3,2,1};

        for(int i = 0; i < lottos.length; i ++){
            if (lottos[i] == 0){
                guess[0]++;
            }
            for(int j = 0; j < win_nums.length; j++){
                if (lottos[i] == win_nums[j]){
                    guess[0]++;
                    guess[1]++;
                }
            }
        }
        answer[0] = rank[guess[0]];  # 변수에 저장하지 않고 바로 return 할 수 없다. 
        answer[1] = rank[guess[1]];
        return answer;
    }
}


# 다른사람 풀이
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        Map<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        int zeroCount = 0;

        for(int lotto : lottos) {   # for(타입 변수명 : 배열 또는 컬렉션)
            if(lotto == 0) {
                zeroCount++;
                continue;
            }
            map.put(lotto, true);  # HashMap에 lotto번호와 bool을 저장
        }


        int sameCount = 0;
        for(int winNum : win_nums) {
            if(map.containsKey(winNum)) sameCount++;  # containsKey(key): 맵에서 인자로 보낸 키가 있으면 true 없으면 false를 반환한다.
        }

        int maxRank = 7 - (sameCount + zeroCount);
        int minRank = 7 - sameCount;
        if(maxRank > 6) maxRank = 6;
        if(minRank > 6) minRank = 6;

        return new int[] {maxRank, minRank};
    }
}
