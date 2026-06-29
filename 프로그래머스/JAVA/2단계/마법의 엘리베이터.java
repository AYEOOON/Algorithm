/*
https://school.programmers.co.kr/learn/courses/30/lessons/148653

[문제 설명]
현재 층수 storey에서 0층으로 이동하려고 한다. 엘리베이터는 다음과 같은 버튼을 가지고 있다.

±1, ±10, ±100, ±1000 ...

버튼을 한 번 누를 때마다 마법의 돌 1개가 소모된다. 목표는 0층으로 이동하기 위해 사용하는 마법의 돌의 최소 개수를 구하는 것이다.

[풀이 아이디어]
이 문제는 가장 낮은 자릿수부터 차례대로 확인하며 해당 자리를 0으로 만드는 비용을 계산하는 그리디 문제이다. 

현재 자릿수의 값(digit)이 5보다 작다면 해당 숫자만큼 내려가는 것이 가장 적은 비용이므로 digit을 정답에 더한다. 
반대로 digit이 5보다 크다면 10 - digit만큼 올려서 다음 자리로 올림을 발생시키는 것이 유리하므로 해당 값을 정답에 더하고 층수에도 반영한다. 
digit이 5인 경우에는 내리는 비용과 올리는 비용이 모두 5로 동일하므로 다음 자릿수를 확인해야 한다. 
  -> 다음 자릿수가 5 이상이면 이후 자릿수에서도 올림이 유리할 가능성이 높기 때문에 올림을 선택하고, 5 미만이면 내림을 선택한다.

각 자릿수의 처리가 끝나면 storey /= 10을 수행하여 다음 자릿수를 확인한다. 
이를 층수가 0이 될 때까지 반복하면 최소 버튼 횟수를 구한다.
*/

class Solution {
    public int solution(int storey) {
        int answer = 0;
        
        while (storey > 0){
            int digit = storey % 10;      // 현재 자리
            
            if (digit < 5){
                answer += digit;
                
            }else if (digit > 5){
                answer += (10-digit);
                storey += (10-digit);
                
            }else if (digit == 5){
                int next = (storey / 10) % 10; // 다음 자리
                if (next >= 5){
                    answer += digit;
                    storey += digit;
                    
                }else{
                    answer += (10-digit);
                }
            }
            storey /= 10;
        }
        return answer;
    }
}
