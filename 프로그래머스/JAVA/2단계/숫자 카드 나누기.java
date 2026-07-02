/*
https://school.programmers.co.kr/learn/courses/30/lessons/135807

[문제 설명]
두 개의 정수 배열이 주어진다. 
한 배열의 모든 원소를 나눌 수 있으면서 다른 배열의 어떤 원소도 나누지 못하는 가장 큰 양의 정수를 구하는 문제이다. 
두 배열 각각을 기준으로 조건을 만족하는 경우를 모두 확인한 뒤, 가능한 값 중 최댓값을 반환하고 조건을 만족하는 값이 없다면 0을 반환한다.

[풀이 아이디어]
배열의 모든 원소를 나눌 수 있는 수는 반드시 그 배열의 최대공약수의 약수이므로, 
가장 큰 값을 구해야 하는 이 문제에서는 각 배열의 최대공약수만 후보로 확인하면 된다. 

먼저 유클리드 호제법을 이용해 arrayA와 arrayB의 최대공약수를 각각 구한다. 
이후 arrayA의 최대공약수가 arrayB의 원소를 하나라도 나누면 조건을 만족하지 못하므로 제외하고, 하나도 나누지 못한다면 정답 후보가 된다. 
반대로 arrayB의 최대공약수도 arrayA의 원소를 하나라도 나누는지 검사하여 조건을 만족하면 정답 후보에 포함한다. 

마지막으로 두 후보 중 더 큰 값을 반환하고, 둘 다 조건을 만족하지 못하면 0을 반환한다.

solution()
 ├── getGcd(arrayA)
 ├── getGcd(arrayB)
 ├── canUse(gcdA, arrayB)
 ├── canUse(gcdB, arrayA)
 └── answer 반환

getGcd()
 └── 배열의 최대공약수 계산

canUse()
 └── 다른 배열의 어떤 원소도 나누지 않는지 검사

gcd()
 └── 유클리드 호제법
*/

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        
        int A_gcd = 0;
        int B_gcd = 0;
        
        A_gcd = getGcd(arrayA);
        B_gcd = getGcd(arrayB);
        
        if (canUse(A_gcd, arrayB)){
            answer = Math.max(answer, A_gcd);
        }
        
        if (canUse(B_gcd, arrayA)){
            answer = Math.max(answer, B_gcd);
        }
        return answer;
    }
    
    public int getGcd(int[] array){
        int result = 0;
        
        for (int num: array){
            result = gcd(result, num);
        }
        
        return result;
    }
    
    public boolean canUse(int gcd, int[] array){
        for (int num: array){
            if (num%gcd == 0){
                return false;
            }
        }
        return true;
    }
    
    public int gcd(int a, int b){
        while(b != 0){
            int r = a%b;
            a = b;
            b = r;
        }
        return a;
    }
}
