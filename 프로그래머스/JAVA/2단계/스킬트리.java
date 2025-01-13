import java.util.*; 

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        String[] sk = skill.split("");
        ArrayList<String> skills = new ArrayList<>();
        for(int i = 0; i < skill_trees.length; i++){
            String[] arr = skill_trees[i].split("");
            for(String s: arr){
                boolean isExist = Arrays.stream(sk).anyMatch(s::equals);
                if(!isExist){
                    skill_trees[i] = skill_trees[i].replace(s, "");
                }
            }
        }
        for(int i = 0; i < skill_trees.length; i++){
            if(skill_trees[i].equals(skill.substring(0, skill_trees[i].length()))){
                answer++;
            }
        }
        return answer;
    }
}
