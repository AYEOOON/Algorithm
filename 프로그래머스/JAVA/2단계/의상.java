import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 0;
        HashMap<String, List<String>> map = new HashMap<>();
        
        for(String[] item: clothes){
            String itemName = item[0];
            String category = item[1];
            
            if(map.containsKey(category)){
                map.get(category).add(itemName);
            }else{
                List<String> newList = new ArrayList<>();
                newList.add(itemName);
                map.put(category, newList);
            }
        }
        int cnt = 1;

        for (String key : map.keySet()) {
            cnt *= map.get(key).size()+1;  // 안 입는 경우를 추가 후, 모두 곱함
        }
        return cnt-1; // 다 안 입는 경우를 제외
    }
}
