import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int cnt = 0;
        for(int[] command: commands){
            int[] arr = Arrays.copyOfRange(array, command[0]-1, command[1]);
            Arrays.sort(arr);
            answer[cnt] = arr[command[2]-1];
            cnt ++;
        }
        return answer;
    }
}
