import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] arr = new int[n];
        Arrays.fill(arr,1);
        
        for(int l:lost) arr[l-1] = 0;

        for(int r:reserve) arr[r-1] += 1;
                    
        for(int i = 0; i<n; i++){
            if(arr[i] == 2){
                if(i-1 >= 0 && arr[i-1] == 0){
                    arr[i] -= 1;
                    arr[i-1] += 1;
                }
                else if(i+1 < n && arr[i+1] == 0){
                    arr[i] -= 1;
                    arr[i+1] += 1;
                }
            }
        }
        
        for(int a:arr){
            if(a >= 1){
                answer += 1;
            }
        }

        return answer;
    }
}
