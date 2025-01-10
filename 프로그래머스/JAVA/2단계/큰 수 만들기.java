import java.util.*;
class Solution {
    public String solution(String number, int k) {
        ArrayList<String> answer = new ArrayList<>();
        ArrayList<String> nums = new ArrayList<>();
        int cnt = k;
        for(String n:number.split("")){
            nums.add(n);
        }
        for(int i = 0; i < nums.size(); i++){
            while(answer.size() > 0 && Integer.parseInt(answer.get(answer.size()-1)) < Integer.parseInt(nums.get(i)) && cnt != 0){
                answer.remove(answer.size()-1);
                cnt--;
            }
            answer.add(nums.get(i));
        }
        return String.join("",answer.subList(0, number.length()-k));
    }
}
