class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int garo = sizes[0][0], sero = sizes[0][1];
        for(int[] s: sizes){
            garo = Math.max(Math.max(s[0], s[1]), garo);
            sero = Math.max(Math.min(s[0], s[1]), sero);
        }
        return garo * sero;
    }
}
