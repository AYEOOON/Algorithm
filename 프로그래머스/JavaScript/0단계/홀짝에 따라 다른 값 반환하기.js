// 양의 정수 n이 매개변수로 주어질 때, 
// n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 
// n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.


// 내 풀이
function solution(n) {
    return n%2 == 1 ? Array.from({length:n}, ((_,i) => i+1)).filter((el)=> el%2==1).reduce((sum,curr)=>sum+curr) :  Array.from({length:n}, ((_,i) => i+1)).filter((el)=> el%2==0).reduce((sum,curr)=>sum+(curr)**2,0)
}


// 다른사람 풀이
function solution(n) {
    if(n%2===1)
      return  (n+1)/2*((n + 1)/2) ;  // n이 홀수일 때는 자연수 거듭 제곱의 합을 구하는 공식을 적용
    else 
      return   n*(n+1)*(n+2)/6;  // n이 짝수일 때는 등차수열의 합 공식을 적용
}
