import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet type = new HashSet<>();
        for(int n: nums) type.add(n);
        return type.size() > nums.length/2 ? nums.length/2 : type.size();
    }
}
