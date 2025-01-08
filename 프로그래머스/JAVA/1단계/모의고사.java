import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = new int[3];
        int[] result = new int[3];
            
        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for(int i = 0; i<answers.length; i++){
            if(answers[i] == first[i%first.length]){
                answer[0]++;
            }
            if(answers[i] == second[i%second.length]){
                answer[1]++;
            }
            if(answers[i] == third[i%third.length]){
                answer[2]++;
            }
        }
        int max = Arrays.stream(answer).max().getAsInt();
        for(int j = 0; j < 3; j++){
            if(answer[j] == max){
                result[j] = j+1;
            }
        }
        return Arrays.stream(result).filter(n->n!=0).toArray();
    }
}
