/*
https://school.programmers.co.kr/learn/courses/30/lessons/92341
: 차량별 총 주차 시간을 구한 뒤 요금 정책에 따라 계산하고, 차량 번호를 오름차순으로 출력하는 문제

[접근]
"상태(Map) + 누적(Map) 분리"

1. 차량 상태 관리(입차/출차)
  - inMap: 현재 주차 중인 차량의 입차 시간
  - totalMap: 차량별 누적 주차 시간
  
  👉 상태와 결과를 분리하는 것이 핵심이다.

2. 기록을 순회하면서 시간 누적
  - IN ⇢ 입차 시간 저장
  - OUT ⇢ (현재 시간 - 입차 시간) 누적

3. 출차 안 된 차량 처리
  - 문제에서 가장 중요한 조건
  - 끝까지 안 나가면 23:59 기준으로 계산

4. 차량 번호 기준 정렬
  - Map은 정렬 안 되므로 따로 정렬 필요

5. 요금 계산 
  - 기본 시간 이하면 기본 요금
  - 초과 시 올림 계산
*/

import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        Map<String, Integer> inMap = new HashMap<>();   // 입차 시간
        Map<String, Integer> totalMap = new HashMap<>(); // 누적 시간
        
        int base_time = fees[0];
        int base_fee  = fees[1];
        int per_time  = fees[2];
        int per_fee   = fees[3];
        
        for (String record: records){
            String[] info = record.split(" ");
            
            String time = info[0];
            String car = info[1];
            String type = info[2];
            
            int minute = convertToMin(time);
            
            if (type.equals("IN")){
                inMap.put(car, minute);
            }else {
                int inTime = inMap.remove(car); // Map.remove(): 값을 꺼내면서 삭제
                totalMap.put(car, totalMap.getOrDefault(car, 0) + (minute - inTime)); // getOrDefault: key 없으면 기본값 반환 (Null 체크 필요 없음)
            }
        }
        for (String car: inMap.keySet()){ // Map.keySet(): key만 가져올 때 사용
            int inTime = inMap.get(car);
            int minute = 23*60+59;
            totalMap.put(car, totalMap.getOrDefault(car, 0) + (minute - inTime));
        }
                        
        List<String> cars = new ArrayList<>(totalMap.keySet());
        Collections.sort(cars);
        
        int[] answer = new int[cars.size()];
        int idx = 0;
        
        for (String car: cars){
            int time = totalMap.get(car);
            int fee = base_fee;
            
            if (time > base_time){
                fee += Math.ceil((time - base_time) / (double) per_time) * per_fee; // Math.ceil + 형변환: (double) 없으면 정수 나눗셈 됨
            }
            answer[idx++] = fee;
        }
        return answer;
    }
    
    public int convertToMin(String time){
        String[] tmp = time.split(":");
        
        return Integer.parseInt(tmp[0]) * 60 + Integer.parseInt(tmp[1]);
    }
}
