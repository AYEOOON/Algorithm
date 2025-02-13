import java.util.*;

class Solution {
    public ArrayList<Integer> solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> sum = new HashMap<>();
        HashMap<String, HashMap<Integer, Integer>> idx = new HashMap<>();
        
        for(int i = 0; i < genres.length; i++){
            sum.put(genres[i], sum.getOrDefault(genres[i], 0) + plays[i]);
            idx.putIfAbsent(genres[i], new HashMap<>());
            idx.get(genres[i]).put(i, plays[i]);
        }
        List<Map.Entry<String, Integer>> genList = new ArrayList<>(sum.entrySet());
        genList.sort((a,b)-> b.getValue().compareTo(a.getValue()));

        for(Map.Entry<String, Integer> genEntry: genList){
            String gen = genEntry.getKey();
            
            List<Map.Entry<Integer, Integer>> songList = new ArrayList<>(idx.get(gen).entrySet());
            songList.sort((a,b)-> b.getValue().compareTo(a.getValue()));
            
            int cnt = 0;
            for(Map.Entry<Integer, Integer> songEntry: songList){
                if(cnt < 2){
                    answer.add(songEntry.getKey());
                    cnt++;
                }
            }
        }
        return answer;
    }
}
