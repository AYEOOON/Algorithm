/*

1. Arrays.asList() 사용
Arrays.asList() 메서드는 배열을 List로 변환하는데 사용

2. Queue 사용
Queue는 자바에서 큐 자료구조를 구현하기 위한 인터페이스이며, LinkedList가 이를 구현

3. String[] 배열을 큐에 넣기
new String[]{} 문법을 사용하여 배열을 생성

4. 문자열 비교
String 객체를 비교할 때 ==를 사용하면 객체의 참조를 비교 -> 문자열의 값이 같은지 비교하려면 equals() 메서드를 사용

5. 문자열 길이와 인덱스 접근
String의 길이는 length() 메서드를 사용

*/
import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        if(!Arrays.asList(words).contains(target)) return 0;
        
        Queue<String[]> Q = new LinkedList<>();
        Q.offer(new String[]{begin, "0"});
        
        while(!Q.isEmpty()){
            String[] current = Q.poll();
            String cur = current[0];
            int cnt = Integer.parseInt(current[1]);
            
            if(cur.equals(target)) return cnt;
            
            for(String word: words){
                int tmp = 0;
                for(int i = 0; i < word.length(); i++){
                    if(cur.charAt(i) != word.charAt(i)){
                        tmp++;
                    }
                }
                if(tmp == 1){
                    Q.offer(new String[]{word, String.valueOf(cnt+1)});
                }
            }
        }
        return 0;
    }
}
